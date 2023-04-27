from rlang import MDPObjectClass


class Manipulator(MDPObjectClass):
    attr_list = ['name', 'num_fingers']

    def __init__(self, name, num_fingers):
        self.name = name
        self.num_fingers = num_fingers
