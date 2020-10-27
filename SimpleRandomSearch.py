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
from Position import Position
from Action import Action
from State import State
from Piece import Piece
from Rook import Rook
from Pawn import Pawn
from King import King
from Queen import Queen
from Bishop import Bishop
from Knight import Knight



class SimpleRandomSearch:
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

        self.m_solution = []
        solutionFound = False
        # current = None
        noSolution = False

        # main loop
        current = self.m_initialState.copy()
        while not (solutionFound):
            if current.isFinal():  # first we check if the state is final
                solutionFound = True
                self.m_finalState = current
            else:
                # generate successors
                possibleActions = self.m_piece.getPossibleActions(current)
                # for a in possibleActions:
                #	print (a.m_initPos, a.m_finalPos)
                # rnd = random.randint(0,len(possibleActions)-1)
                # print(len(possibleActions), rnd)
                if len(possibleActions) == 0:
                    break
                action = possibleActions[random.randint(0, len(possibleActions) - 1)]
                # print(action.m_initPos, action.m_finalPos)
                self.m_solution.append(action)
                self.m_cost += action.getCost()
                current = current.applyAction(action)

        return current


# main method


if __name__ == '__main__':
    # print(len(sys.argv))

    if (len(sys.argv) != 6):
        print("\n**Sorry, correct usage require 5 params:");
        print("Board size: int.");
        print("Density: (0.1,1]. Probability for each piece to be included.");
        print("Seed1: int. To initialize the problem instance random number generator (for reproducibility)");
        print("Agent: {0,1,2,3,4,5} standing for white pawn, rook, bishop, knight, queen or king.");
        print("Seed2: int. To initialize the Random Search instance random number generator (for reproducibility)");
        sys.exit()
    else:
        size = int(sys.argv[1])
        density = float(sys.argv[2])
        seed1 = int(sys.argv[3])
        agent = int(sys.argv[4])
        seed2 = int(sys.argv[5])

        if size < 4:
            print("\nSorry: board to small, modified to 4")
            size = 4

        if density < 0.1 or density > 1.0:
            print("\nSorry: bad density value, modified to 0.25")
            density = 0.25

        if density * 32 > size * size:
            print("\nSorry: too much pieces for the board size, modifying density to 0.25")
            density = 0.25

        if agent < 0 or agent > 11:
            print("\nSorry: bad selected agent, modified to 1 (white rook)")
            agent = Utils.wRook

        # getting the initial state
        state = Utils.getProblemInstance(size, density, seed1, agent)
        Utils.printBoard(state)

        srs = SimpleRandomSearch(state, seed2)
        finalState = srs.doSearch()

        if srs.m_finalState == None:
            print("\nSorry, no solution found ....")
        else:
            print("Solution length: %d" % len(srs.m_solution))
            print("Solution cost:   %f" % srs.m_cost)

            print("Solution:\n")
            for i in range(len(srs.m_solution)):
                print("%d : " % (i + 1), end="")
                print(srs.m_solution[i])
            Utils.printBoard(finalState)

        print()
