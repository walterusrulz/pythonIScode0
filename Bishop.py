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
        ln = []
        ln += self.getVerticalDownMoves()

        return ln
