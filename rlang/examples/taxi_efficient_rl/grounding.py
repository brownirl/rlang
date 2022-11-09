import context
import rlang
from rlang.grounding import MDPObject


class TaxiClass(MDPObject):
    attr_list = ['name', 'touch_n', 'touch_s', 'touch_e', 'touch_w', 'on_destination', 'on_passenger', 'location']

    def __init__(self, name, touch_n=False, touch_s=False, touch_e=False, touch_w=False, on_destination=False, on_passenger=False, location=None):
        self.name = name
        self.touch_n = touch_n
        self.touch_s = touch_s
        self.touch_e = touch_e
        self.touch_w = touch_w
        self.on_destination = on_destination
        self.on_passenger = on_passenger
        self.location = location


class PassengerClass(MDPObject):
    attr_list = ['name', 'location', 'in_taxi']

    def __init__(self, name, location=None, in_taxi=False):
        self.name = name
        self.location = location
        self.in_taxi = in_taxi

