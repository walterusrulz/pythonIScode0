import sys
import Utils
from SimpleRandomSearch import SimpleRandomSearch
from BreadthFirst import BreadthFirst
from DepthFirst import DepthFirst
from UniformCost import UniformCost
from Greedy import Greedy
from Astar import Astar

######ENTRY POINT#######################################################################################################


if __name__ == '__main__':
    # print(len(sys.argv))
    algos = ["SimpleRandom","BreadthFirst", "DepthFirst", "Uniform", "Greedy", "Astar"]
    if (len(sys.argv) != 7):
        print("\n**Sorry, correct usage require 5 params:");
        print("Board size: int.");
        print("Density: (0.1,1]. Probability for each piece to be included.");
        print("Seed1: int. To initialize the problem instance random number generator (for reproducibility)");
        print("Agent: {0,1,2,3,4,5} standing for white pawn, rook, bishop, knight, queen or king.");
        print("Seed2: int. To initialize the Random Search instance random number generator (for reproducibility)");
        print("Search algorithm: available SimpleRandom, BreadthFirst, DepthFirst", "Uniform", "Greedy", "Astar")
        sys.exit()
    else:
        size = int(sys.argv[1])
        density = float(sys.argv[2])
        seed1 = int(sys.argv[3])
        agent = int(sys.argv[4])
        seed2 = int(sys.argv[5])
        algo = sys.argv[6]

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
        if algo not in algos:
            print("\nSorry: bad selected algorithm, defaulting to SimpleRandom")
            algo = algos[0]
        # getting the initial state
        state = Utils.getProblemInstance(size, density, seed1, agent)
        Utils.printBoard(state)
        if algo == algos[0]:
            srs = SimpleRandomSearch(state, seed2)
            finalState = srs.doSearch()
        elif algo == algos[1]:
            srs = BreadthFirst(state, seed2)
            finalState = srs.doSearch()
            srs.m_solution.reverse()
            print("Solution steps : %d" %len(srs.m_solution))
            print("Generated nodes: %d" %srs.nGenerated)
            print("Visited nodes: %d" %srs.nVisited)
            print("Expanded nodes: %d" %srs.nExpanded)
        elif algo == algos[2]:
            srs = DepthFirst(state, seed2)
            finalState = srs.doSearch()
            srs.m_solution.reverse()
            print("Solution steps : %d" %len(srs.m_solution))
            print("Generated nodes: %d" % srs.nGenerated)
            print("Visited nodes: %d" % srs.nVisited)
            print("Expanded nodes: %d" % srs.nExpanded)
        elif algo == algos[3]:
            srs = UniformCost(state, seed2)
            finalState = srs.doSearch()
            srs.m_solution.reverse()
            print("Solution steps : %d" %len(srs.m_solution))
            print("Generated nodes: %d" % srs.nGenerated)
            print("Visited nodes: %d" % srs.nVisited)
            print("Expanded nodes: %d" % srs.nExpanded)
        elif algo == algos[4]:
            srs = Greedy(state, seed2)
            finalState = srs.doSearch()
            srs.m_solution.reverse()
            print("Solution steps : %d" %len(srs.m_solution))
            print("Generated nodes: %d" % srs.nGenerated)
            print("Visited nodes: %d" % srs.nVisited)
            print("Expanded nodes: %d" % srs.nExpanded)
        elif algo == algos[5]:
            srs = Astar(state, seed2)
            finalState = srs.doSearch()
            srs.m_solution.reverse()
            print("Solution steps : %d" %len(srs.m_solution))
            print("Generated nodes: %d" % srs.nGenerated)
            print("Visited nodes: %d" % srs.nVisited)
            print("Expanded nodes: %d" % srs.nExpanded)

        if srs.m_finalState == None:
            print("\nSorry, no solution found ....")
        else:
            print("Solution length: %d" % len(srs.m_solution))
            print("Solution cost:   %f" % srs.m_cost)

            print("Solution:\n")
            for i in range(len(srs.m_solution)):
                print("%d : " % (i + 1), end="")
                print(srs.m_solution[i])
            Utils.printBoard(finalState.state)

        print()
