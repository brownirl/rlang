import context
from rlang.grounding import ParameterizedAction, MDPObject, MDPObjectGrounding


class Things(MDPObject):
    def __init__(self, name):
        super().__init__(name)


block = MDPObjectGrounding(Things('block'), name='block')


def go_skill(x, y, z, **kwargs):
    print(f"I'm going to {x}, {y}, {z}")


def grab_skill(ob, **kwargs):
    print(f"I'm grabbing {ob}")


go = ParameterizedAction(go_skill, name='go')
grab = ParameterizedAction(grab_skill, name='grab')
