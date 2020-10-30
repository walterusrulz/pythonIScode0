# import java.util.ArrayList;
# import java.util.Hashtable;
# import java.util.Random;

# this class implements a simple search method which explores a single sequence of actions.
# The process is quite simple. At each state we look for the agent possible actions and choose one at random.
# The action is then applied and if the new state is final, the method stops returning the list of applied actions.
# On the other hand, we iterate.

import sys
import random
import Utils
from Piece import Piece
from Rook import Rook
from Pawn import Pawn
from King import King
from Queen import Queen
from Bishop import Bishop
from Knight import Knight



class Search:
    # member variables
    m_initialState = None
    m_seedRS = -1
    # Random m_generator = null;
    # m_solution = None

    m_cost = 0.0
    m_piece = Piece()
    m_finalState = None

    # constructor
    def __init__(self, s0, seed):
        self.m_initialState = s0
        self.m_seedRS = seed
        # m_generator = new Random(m_seedRS);
        self.m_cost = 0.0
        random.seed(seed)

        if s0.m_agent == Utils.wPawn:
            self.m_piece = Pawn(0)
        elif s0.m_agent == Utils.bPawn:
            self.m_piece = Pawn(1)
        elif s0.m_agent == Utils.wRook:
            self.m_piece = Rook(0)
        elif s0.m_agent == Utils.bRook:
            self.m_piece = Rook(1)
        elif s0.m_agent == Utils.wKing:
            self.m_piece = King(0)
        elif s0.m_agent == Utils.bKing:
            self.m_piece = King(1)
        elif s0.m_agent == Utils.wQueen:
            self.m_piece = Queen(0)
        elif s0.m_agent == Utils.bQueen:
            self.m_piece = Queen(1)
        elif s0.m_agent == Utils.wBishop:
            self.m_piece = Bishop(0)
        elif s0.m_agent == Utils.bBishop:
            self.m_piece = Bishop(1)
        elif s0.m_agent == Utils.wKnight:
            self.m_piece = Knight(0)
        elif s0.m_agent == Utils.bKnight:
            self.m_piece = Knight(1)

        else:
            # define the rest of pieces
            print("Chess piece not implemented")
            sys.exit()

    # search method
    def doSearch(self):
        return None


