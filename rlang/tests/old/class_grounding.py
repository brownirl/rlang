from rlang import MDPObject


class Manipulator(MDPObject):
    attr_list = ['name', 'num_fingers']

    def __init__(self, name, num_fingers):
        self.name = name
        self.num_fingers = num_fingers
