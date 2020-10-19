import Utils
from Piece import Piece


# this class implements the getPossibleActions for each type of piece

class King(Piece):

    # constructor
    def __init__(self, color):
        self.m_color = color

        if color == 0:
            self.m_type = Utils.wKing
        else:
            self.m_type = Utils.bKing

    # this method must be completed with all the possible pieces
    def getPossibleActions(self, state):
        listing = []
        listing += self.get_immediate_moves(state)

        return listing
