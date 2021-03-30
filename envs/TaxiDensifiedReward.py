from simple_rl.tasks.taxi.TaxiOOMDPClass import TaxiOOMDP
from collections import defaultdict

class TaxiDense(TaxiOOMDP):
    def __init__(self, width, height, agent, walls, passengers, slip_prob=0, gamma=0.99):
        TaxiOOMDP.__init__(self,width, height, agent, walls, passengers, slip_prob=0, gamma=0.99)
        self.picked_up = defaultdict(lambda: None)
        #self.step_cost = 0 


    def _taxi_reward_func(self, state, action, next_state):
        '''
        Overload Reward function.
        Args:
            state (OOMDP State)
            action (str)
            next_state (OOMDP State)

        Returns
            (float)
        '''
        # r = super()._taxi_reward_func(state, action, next_state)
        # dis = self.__distance_passengers_to_dest(state)/(self.width + self.height)
        # dis_prime = self.__distance_passengers_to_dest(next_state)/(self.width + self.height)
        # return r + (self.gamma * dis_prime - dis)*(-0.01)
        r = super()._taxi_reward_func(state, action, next_state)

        if (action == "dropoff" and state.get_objects_of_class("agent")[0].get_attribute("has_passenger") != 1):
            return -0.5 + r 
        return r
        



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

    def __distance_passengers_to_dest(self, state):
        dis = 0
        agent = state.get_first_obj_of_class("agent")
        for p in state.get_objects_of_class("passenger"):
            dis += abs(p.get_attribute("dest_x") - p.get_attribute("x")) + abs(p.get_attribute("dest_y") - p.get_attribute("y"))
        return dis/len(state.get_objects_of_class("passenger"))