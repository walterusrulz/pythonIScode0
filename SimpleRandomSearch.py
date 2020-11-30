# import java.util.ArrayList;
# import java.util.Hashtable;
# import java.util.Random;

# this class implements a simple search method which explores a single sequence of actions.
# The process is quite simple. At each state we look for the agent possible actions and choose one at random.
# The action is then applied and if the new state is final, the method stops returning the list of applied actions.
# On the other hand, we iterate.
import copy
import sys
import random
import Utils
from Search import Search


class SimpleRandomSearch(Search):

    # constructor
    def __init__(self, s0, seed):
        super().__init__(s0, seed)

    # search method
    def doSearch(self):

        self.m_solution = []
        solutionFound = False
        # current = None
        noSolution = False

        # main loop
        current = copy.deepcopy(self.m_initialState)
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


