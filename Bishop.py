import Utils
from Piece import Piece


class Bishop(Piece):

    # constructor
    def __init__(self, color):
        self.m_color = color

        if color == 0:
            self.m_type = Utils.wBishop
        else:
            self.m_type = Utils.bBishop

    def getPossibleActions(self, state):
        l = []
        l = self.getUpLeftMoves(state)
        l += self.getUpRightMoves(state)
        l += self.getDownLeftMoves(state)
        l += self.getDownRightMoves(state)

        return l
