'''
    Hierarchical RL Agent
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: March 2021
'''

class HierarchicalAgent:
    def __init__(self, actions, options, outer_agent, inner_agent, discount_factor=0.99):
        self._actions = actions
        self._options = options
        self._outer_agent = OuterAgent(options, outer_agent)
        self._inner_agent = InnerAgent(actions, options, inner_agent)
        self._gamma = discount_factor
        self._t = 0
        self._r = 0
        self._curr_option = None

    def act(self, state):
        r = state['reward']
        self._r += r * self._gamma ** self._t # accumulates discounted reward
        if self._curr_option is None or not self.inner_is_executing(state):
            s = {'observation': state['observation'], 'reward': self._r, 'done': state['done']}
            o = self._outer_agent.act(s)
            self._curr_option = o
            self._r, self._t = 0,0
            self._inner_agent.execute(o) # start option o
        return self.inner_agent_act(state)
    
    def inner_agent_act(self, state):
        return self._inner_agent.act(state)

    def inner_is_executing(self, state):
        return self._inner_agent.is_executing(state)

class SubgoalHierarchicalAgent(HierarchicalAgent):
    def inner_agent_act(self, state):
        s =  {'observation': state['observation'], 'reward': -.1, 'done': state['done']} # zero reward while subgoal is not reached
        return self._inner_agent.act(s)

    def inner_is_executing(self, state):
        if self._inner_agent.is_executing(state): # not terminated
            return True
        else:
            if (self._curr_option.termination(state['observation'])): # goal reached.
                s =  {'observation': state['observation'], 'reward': 1, 'done': state['done']}
                self._inner_agent.act(s) # extra step to update inner agent with intrinsic reward
            return False 

class InnerAgent:
    def __init__(self, actions, options, agent_factory):
        self._executing_agent = None
        self._executing_option = None
        agents = [(o._id, agent_factory(o)) for o in options]
        self._option_agents = dict(agents)

    def execute(self, option):
        self._executing_option = option
        self._executing_agent = self._option_agents[option._id]

    def act(self, state):
        action = self._executing_agent.act(state)
        return action
    
    def stop(self, state):
        self._executing_agent.stop(state)

    def is_executing(self, state):
        if (self._executing_agent is None or self._executing_option is None):
            return False
        if (self._executing_option.terminated(state['observation'])):
            self.stop(state)
            return False
        return True
    
    def eval(self, state):
        return self._executing_agent.eval(state)

class OuterAgent:
    def __init__(self, options, agent_factory):
        self._agent = agent_factory(options)

    def act(self, state):
        return self._agent.act(state)

    def eval(self, state):
        return self._agent.eval(state)