# agents directory

> This directory has to be move out of the main LMDP/RLang classes as it is logically separated from them.

* AbstractValueIterationClass.py: Simple RL-based Value Iteration for FourRoom Planning example (examples/four_room/four_room_smdp_example.py)
* Agent.py: Basic Agent interface. Possibly to refactor other classes based on this.
* all_hierarchical_dqn.py: Hierarchical DDQN Agent and supporting classes based on [ALL](https://autonomous-learning-library.readthedocs.io/en/stable/) 
* all_option_dqn.py: Adaptation of DDQN agent (based on [ALL](https://autonomous-learning-library.readthedocs.io/en/stable/)) to work with Options.
* dqn.py: DDQN preset based on [ALL](https://autonomous-learning-library.readthedocs.io/en/stable/)
* factories.py: Agent Factories for Q-Learning, Vanilla DQN and others. To be deprecated/refactored. It contains classes being used by the hierarchical Q-Learning in Taxi (examples/taxi/hierarchical_q.py) and implementation based on [ALL](https://autonomous-learning-library.readthedocs.io/en/stable/) (v0.6 instead of v0.7)
* LangAgentClass.py (**To be deprecated**): Old RLang-informed Agent class implemented as a Wrapper Pattern that gives the possibility to set a LMDP object for the agent to use. 
* option_dqn.py (**To be deprecated**): Old DQN with options using [ALL](https://autonomous-learning-library.readthedocs.io/en/stable/) v0.6 
* QLearningLangAgentClass.py: RLang-informed Q-Learning Agent based on Simple RL
* ReinforceMLPAgentClass.py (**to be deleted**): REINFORCE agent to be deleted.
* ReinforceMLPLangAgentClass.py (**to be deleted**): REINFORCE agent to be deleted.
* rlang_agent_builder.py: Abstract Interface for RLang-informed Agent Factories.
* rlang_hdqn.py: RLang-informed hierarchical DDQN
* RMaxLangAgentClass.py: RLang-informed RMax agent based on Simple RL
* SarsaAgentClass.py (possibly **to be deleted**): SARSA agent implementation for Simple RL
* SarsaLangAgentClass.py (possibly **to be deleted**): RLang-informed SARSA agent 
* simple_rl_agent.py: Adapts Agent Interface (above) to Simple RL Agent interface.
