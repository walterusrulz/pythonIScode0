import copy

from State import State


class Node:
    # Auto constructor
    def __init__(self):
        self.progenitor = None
        self.state = None
        self.hashcode = -1

    def __init__(self, progenitor, state, action):
        self.progenitor = progenitor
        self.state = state
        self.hashcode = -1
        self.action = action


