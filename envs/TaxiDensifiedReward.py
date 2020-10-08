from simple_rl.tasks.taxi.TaxiOOMDPClass import TaxiOOMDP
from collections import defaultdict

class TaxiDense(TaxiOOMDP):
    def __init__(self, width, height, agent, walls, passengers, slip_prob=0, gamma=0.99):
        TaxiOOMDP.__init__(self,width, height, agent, walls, passengers, slip_prob=0, gamma=0.99)
        self.picked_up = defaultdict(lambda: None)
        #self.step_cost = 0 


    def _taxi_reward_func(self, state, action, next_state=None):
        '''
        Overload Reward function.
        Args:
            state (OOMDP State)
            action (str)
            next_state (OOMDP State)

        Returns
            (float)
        '''
        #_error_check(state, action)

        # If agent is dropping off.
        agent = state.get_first_obj_of_class("agent")
        # Stacked if statements for efficiency.
        if action == "dropoff":
           

            # Check to see if all passengers at destination.
            if agent.get_attribute("has_passenger"):
                for p in state.get_objects_of_class("passenger"):
                    if p.get_attribute("x") != p.get_attribute("dest_x") or p.get_attribute("y") != p.get_attribute("dest_y"):
                        return 0 - self.step_cost
                return 1 - self.step_cost
        elif action == "pickup":
            for p in state.get_objects_of_class("passenger"):
                    if p.get_attribute("x") == agent.get_attribute("x") and p.get_attribute("y") == agent.get_attribute("y") and self.picked_up[p] is not None:
                        self.picked_up[p] = 1 # passenger picked up once
                        return 0.5 - self.step_cost
                    elif p.get_attribute("x") == agent.get_attribute("x") and p.get_attribute("y") == agent.get_attribute("y"):
                        return -0.5 - self.step_cost
        else:
            dis = self._min_distance_to_passengers(state)
            return -0.01*dis/2 - self.step_cost
                    
        return 0 - self.step_cost

    def _min_distance_to_passengers(self, state):
        min_distance = 1e10
        agent = state.get_first_obj_of_class("agent")
        
        for p in state.get_objects_of_class("passenger"):
            if self.picked_up[p] is None: # if passenger has not been picked up yet
                dis = abs(agent.get_attribute("x") - p.get_attribute("x")) + abs(agent.get_attribute("y") - p.get_attribute("y"))
                if dis < min_distance:
                    min_distance = dis
            else:
                min_distance = 0
                #dis = abs(agent.get_attribute("x") - p.get_attribute("x")) + abs(agent.get_attribute("y") - p.get_attribute("y"))   
        return min_distance