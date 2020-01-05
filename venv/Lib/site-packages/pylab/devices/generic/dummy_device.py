import random

class DummyDevice():

    def __init__(self):
        pass

    def get_value(self):
        return random.randint(0,101)
