import sys
import random
from collections import deque

import Utils
from Search import Search
from Node import Node
import queue
import copy

class DepthFirst(Search):
    # constructor
    def __init__(self, s0, seed):
        super().__init__(s0, seed)

    # search method
    def doSearch(self):
        self.m_solution = []
        visitedNodes = set()  # something more efficient needed
        open_nodes = deque() # LIFO Queue
        # main loop
        current = copy.deepcopy(self.m_initialState)
        root_node = Node(None, current, None)
        root_node.hashcode = hash(root_node.state)
        open_nodes.append(root_node)
        self.nGenerated += 1
        while len(open_nodes) > 0:  # while the list is not empty
            current_node = open_nodes.pop()
            if current_node.hashcode not in visitedNodes:
                visitedNodes.add(current_node.hashcode)
                if current_node.state.isFinal():  # first we check if the state is final
                    self.nVisited += 1
                    self.recover_path(current_node)
                    self.m_finalState = current_node.state
                    return current_node
                else:
                    # generate successors
                    possibleActions = self.m_piece.getPossibleActions(current_node.state)  # self references the Piece
                    for each_action in possibleActions:
                        # print(each_action)
                        state_generated0 = copy.deepcopy(current_node.state)
                        state_generated = state_generated0.applyAction(each_action)
                        node_generated = Node(current_node, state_generated, each_action)
                        node_generated.hashcode = hash(node_generated.state)
                        open_nodes.append(node_generated)
                        self.nGenerated += 1
                    self.nExpanded += 1  # adding just explored node to visited
                    self.nVisited += 1
        return current_node

    def recover_path(self, current_node):
        while not current_node.progenitor is None:
            self.m_solution.append(current_node.action)
            self.m_cost += current_node.action.getCost()
            current_node = current_node.progenitor
        return None
