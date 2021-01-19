'''
    Markov Features Class
        - Real Vector Functions of an experience tuple SxAxS
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''


from lmdp.grounding.real.RealExpressionClass import RealExpression

class MarkovFeature(RealExpression):

    def __init__(self, function, dimension=1):
        RealExpression.__init__(self, function, dimension=dimension, domain=["state", "action", "next_state"])