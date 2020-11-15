import sys
import random
from collections import deque

import Utils
from Search import Search
from Node import Node
import queue
import copy


class UniformCost(Search):
    # constructor
    def __init__(self, s0, seed):
        super().__init__(s0, seed)

    # search method
    def doSearch(self):
        self.m_solution = []
        visitedNodes = set()  # something more efficient needed
        open_nodes = queue.PriorityQueue()  # FIFO Queue
        # main loop
        current = copy.deepcopy(self.m_initialState)
        root_node = Node(None, current, None)
        root_node.hashcode = hash(root_node.state)
        open_nodes.put((root_node.cost, root_node.id, root_node))  # a triple
        self.nGenerated += 1
        while open_nodes.qsize() > 0:  # while the list is not empty
            currentTriple = open_nodes.get()
            current_node = currentTriple[2]  # selecting the node, not the cost
            if current_node.hashcode not in visitedNodes:
                visitedNodes.add(current_node.hashcode)
                if current_node.state.isFinal():  # first we check if the state is final
                    self.nVisited += 1
                    self.recover_path(current_node)
                    self.m_finalState = current_node.state
                    return current_node.state
                else:
                    # generate successors
                    possibleActions = self.m_piece.getPossibleActions(current_node.state)  # self references the Piece
                    for each_action in possibleActions:
                        # print(each_action)
                        state_generated0 = copy.deepcopy(current_node.state)
                        state_generated = state_generated0.applyAction(each_action)
                        node_generated = Node(current_node, state_generated, each_action)
                        node_generated.hashcode = hash(node_generated.state)
                        node_generated.cost = current_node.cost + each_action.getCost()  # calculate cost up to here
                        open_nodes.put((node_generated.cost, node_generated.id, node_generated))  # a triple
                        # first priority is
                        # cost, second succession id
                        self.nGenerated += 1
                    self.nExpanded += 1  # adding just explored node to visited
                    self.nVisited += 1
        return current_node.state

    def recover_path(self, current_node):
        while not current_node.progenitor is None:
            self.m_solution.append(current_node.action)
            self.m_cost += current_node.action.getCost()
            current_node = current_node.progenitor
        return None
