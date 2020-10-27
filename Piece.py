# import java.util.ArrayList;

# this class implements the getPossibleActions for each type of piece

import Utils
from Position import Position
from Action import Action
from State import State


class Piece:
    # this method must be completed with all the possible pieces

    def __init__(self):
        m_color = -1
        m_type = -1

    def getPossibleActions(self, state):

        return None  # never arrive here

    # horizontal left moves
    def getHorizontalLeftMoves(self, state):
        l = []
        # agentColor = self.m_color
        agentColor = 0
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col

        busyCell = False
        for c in range(col0 - 1, -1, -1):
            if not busyCell:
                if state.m_board[row0][c] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(row0, c))
                    l.append(action)
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[row0][c]):  # capture piece
                        action = Action(state.m_agentPos, Position(row0, c))
                        l.append(action)

        return l

    # horizontal right moves
    def getHorizontalRightMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col

        busyCell = False
        for c in range(col0 + 1, state.m_boardSize):
            if not busyCell:
                if state.m_board[row0][c] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(row0, c))
                    l.append(action)
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[row0][c]):  # capture piece
                        action = Action(state.m_agentPos, Position(row0, c))
                        l.append(action)

        return l

    # vertical up moves
    def getVerticalUpMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col

        busyCell = False
        for r in range(row0 - 1, -1, -1):
            if not busyCell:
                if state.m_board[r][col0] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(r, col0))
                    l.append(action)
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[r][col0]):  # capture piece
                        action = Action(state.m_agentPos, Position(r, col0))
                        l.append(action)
        return l

    # vertical down moves
    def getVerticalDownMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col

        busyCell = False
        for r in range(row0 + 1, state.m_boardSize):
            if not busyCell:
                if state.m_board[r][col0] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(r, col0))
                    l.append(action)
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[r][col0]):  # capture piece
                        action = Action(state.m_agentPos, Position(r, col0))
                        l.append(action)

        return l

    def getUpLeftMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

        busyCell = False
        r_range = range(row0 - 1, -1, -1)
        c_range = range(col0 - 1, -1, -1)
        x = zip(r_range, c_range)
        for r, c in x:
            if not busyCell:
                if state.m_board[r][c] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(r, c))
                    l.append(action)
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[r][c]):  # capture piece
                        action = Action(state.m_agentPos, Position(r, c))
                        l.append(action)

        return l

    def getUpRightMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

        busyCell = False
        r_range = range(row0 - 1, -1, -1)
        c_range = range(col0 + 1, state.m_boardSize)
        x = zip(r_range, c_range)
        for r, c in x:
            if not busyCell:
                if state.m_board[r][c] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(r, c))
                    l.append(action)
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[r][c]):  # capture piece
                        action = Action(state.m_agentPos, Position(r, c))
                        l.append(action)

        return l

    def getDownLeftMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

        busyCell = False
        r_range = range(row0 + 1, state.m_boardSize)
        c_range = range(col0 - 1, -1, -1)
        x = zip(r_range, c_range)
        for r, c in x:
            if not busyCell:
                if state.m_board[r][c] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(r, c))
                    l.append(action)
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[r][c]):  # capture piece
                        action = Action(state.m_agentPos, Position(r, c))
                        l.append(action)

        return l

    """Done?"""

    def getDownRightMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

        busyCell = False
        r_range = range(row0 + 1, state.m_boardSize)
        c_range = range(col0 + 1, state.m_boardSize)
        x = zip(r_range, c_range)
        for r, c in x:
            if not busyCell:
                if state.m_board[r][c] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(r, c))
                    l.append(action)
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[r][c]):  # capture piece
                        action = Action(state.m_agentPos, Position(r, c))
                        l.append(action)

        return l


    def get_immediate_moves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col
        final_element = state.m_boardSize
        for r in range(row0 - 1, row0 + 2):
            for c in range(col0 - 1, col0 + 2):
                if r in range(0, final_element) and c in range(0, final_element):
                    # print("In range position")
                    # print(r,c)
                    if state.m_board[r][c] == Utils.empty:  # add action
                        # print("Empty square")
                        action = Action(state.m_agentPos, Position(r, c))
                        l.append(action)
                    else:
                        if agentColor != Utils.getColorPiece(state.m_board[r][c]):  # capture piece
                            # print("Opponent square")
                            # print(r, c)
                            action = Action(state.m_agentPos, Position(r, c))
                            l.append(action)

        return l

    def knight_moves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col
        final_element = state.m_boardSize
        r_range = [-2, -2, -1, -1, 1, 1, 2, 2]
        c_range = [1, -1, 2, -2, 2, -2, 1, -1]
        valid = range(0, final_element)
        x = zip(r_range, c_range)
        for r_gen, c_gen in x:
            r, c = row0 + r_gen, col0 + c_gen;
            if r in valid and c in valid:
                if state.m_board[r][c] == Utils.empty:  # add action
                    # print("Empty square")
                    action = Action(state.m_agentPos, Position(r, c))
                    l.append(action)
                else:
                    if agentColor != Utils.getColorPiece(state.m_board[r][c]):  # capture piece
                        # print("Opponent square")
                        # print(r, c)
                        action = Action(state.m_agentPos, Position(r, c))
                        l.append(action)
        return l
