import sys
import random
import Utils
from Search import Search
from Node import Node
import queue


class BreadthFirst(Search):
    # constructor
    def __init__(self, s0, seed):
        super().__init__(s0, seed)

    # search method
    def doSearch(self):
        visitedNodes = set()  # something more efficient needed
        open_nodes = queue.Queue()  # FIFO Queue
        # main loop
        current = self.m_initialState.copy()
        root_node = Node(None, current, None)
        root_node.hashcode = root_node.state.calculate_hash()
        open_nodes.put(root_node)
        self.nGenerated += 1

        while open_nodes.qsize() > 0:  # while the list is not empty
            current_node = open_nodes.get()
            if current_node.hashcode not in visitedNodes:
                if current_node.state.isFinal():  # first we check if the state is final
                    self.nVisited += 1
                    self.recover_path(current_node)
                    self.m_finalState = current_node.state
                    return current_node
                else:
                    # generate successors
                    possibleActions = self.m_piece.getPossibleActions(current_node.state)  # self references the Piece
                    for each_action in possibleActions:
                        state_generated = current_node.state.applyAction(each_action)
                        node_generated = Node(current_node, state_generated, each_action)
                        node_generated.hashcode = node_generated.state.calculate_hash()
                        open_nodes.put(node_generated)
                        self.nGenerated += 1
                    visitedNodes.add(current_node.hashcode)  # adding just explored node to visited
                    self.nVisited += 1
        return current_node

    def recover_path(self, current_node):
        while not current_node.progenitor is None:
            self.m_solution.append(current_node.action)
            self.m_cost += current_node.action.getCost()
            current_node = current_node.progenitor
        return None
