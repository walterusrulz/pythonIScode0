import copy

from State import State


class Node:
    id = 0
    # Auto constructor
    def __init__(self):
        self.progenitor = None
        self.state = None
        self.hashcode = -1
        self.cost = 0
        Node.id += 1  # generation id

    def __init__(self, progenitor, state, action):
        self.progenitor = progenitor
        self.state = state
        self.hashcode = -1
        self.action = action
        self.cost = 0
        Node.id += 1  # generation id

