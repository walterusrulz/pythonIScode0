import Utils
from Piece import Piece


# this class implements the getPossibleActions for each type of piece

class Queen(Piece):

    # constructor
    def __init__(self, color):
        self.m_color = color

        if color == 0:
            self.m_type = Utils.wQueen
        else:
            self.m_type = Utils.bQueen

    # this method must be completed with all the possible pieces
    def getPossibleActions(self, state):
        print("Inside possibleActions")
        l = []

        l = self.getHorizontalLeftMoves(state)
        l += self.getHorizontalRightMoves(state)
        l += self.getVerticalDownMoves(state)
        l += self.getVerticalUpMoves(state)
        l = self.getUpLeftMoves(state)
        l += self.getUpRightMoves(state)
        l += self.getDownLeftMoves(state)
        l += self.getDownRightMoves(state)

        return l