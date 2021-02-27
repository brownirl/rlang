import sys, os
sys.path.append(os.path.abspath("./lmdp"))

# simple_rl environments
from simple_rl.tasks import TaxiOOMDP

# LMDP
from lmdp import LMDP
from lmdp.agents import ReinforceMLPAgent

if __name__ == "__main__":

    # initialize MDP
    width, height = 9, 9
    agent = {"x":1, "y":1, "has_passenger":0}
    passengers = [{"x":4, "y":4, "dest_x":1, "dest_y":1, "in_taxi":0}]
    taxi_mdp = TaxiOOMDP(width, height, agent=agent, passengers=passengers, walls=[])
    
    # agents

    # lmdp
    lmdp = lmdp.LMDP(taxi_mdp, factor_names=["x", "y", "has_passenger", "dest_x", "dest_y", "in_taxi"])