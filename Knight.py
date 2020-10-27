import Utils
from Piece import Piece


class Knight(Piece):

    # constructor
    def __init__(self, color):
        self.m_color = color

        if color == 0:
            self.m_type = Utils.wKnight
        else:
            self.m_type = Utils.bKnight

    def getPossibleActions(self, state):

        return self.knight_moves(self, state)
