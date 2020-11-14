# This class contains the information needed to represent a state 
# and some useful methods

import sys
import copy
import Utils


class State:
    m_board = None
    m_agentPos = None
    m_agent = -1  # the type of piece
    m_color = 0  # 0 for white, 1 for black
    m_boardSize = -1
    hash_number = -1


    #def __hash__(self):
    #   return hash((self.m_board, self.m_agentPos, self.m_agent, self.m_color, self.m_boardSize))

    # constructor
    def __init__(self, board, position, agent):
        self.m_board = board
        self.m_agentPos = position
        self.m_agent = agent
        if (self.m_agent > 11):
            print("\n*** Invalid piece ***\n")
            sys.exit(0)
        else:
            if (self.m_agent > 5):
                self.m_color = 1  # black

        self.m_boardSize = len(board[0])
        self.hash_number = -1

    # compares if the current state is final, i.e. the agent is in the last row
    def isFinal(self):
        if (self.m_agentPos.row == self.m_boardSize - 1):
            return True
        else:
            return False



    # apply a given action over the current state -which remains unmodified. Return a new state

    def applyAction(self, action):
        newState = copy.deepcopy(self)
        newState.m_board[action.m_initPos.row][action.m_initPos.col] = Utils.empty
        newState.m_board[action.m_finalPos.row][action.m_finalPos.col] = newState.m_agent
        newState.m_agentPos = action.m_finalPos

        return newState

    def calculate_hash(self):
        my_hash = hash(self)
        return my_hash
