import sys
import Utils
from SimpleRandomSearch import SimpleRandomSearch
from BreadthFirst import BreadthFirst
from DepthFirst import DepthFirst
from UniformCost import UniformCost
from Greedy import Greedy
from Astar import Astar
import pandas

######ENTRY POINT#######################################################################################################


if __name__ == '__main__':
    # print(len(sys.argv))
    # solution data
    piece_data = []
    size_data = []
    prob_data = []
    steps_sol = []
    cost_sol = []
    generated_nodes = []
    explored_nodes = []
    expanded_nodes = []

    algos = ["SimpleRandom", "BreadthFirst", "DepthFirst", "Uniform", "Greedy", "Astar"]
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

        if algo == algos[0]:
            state = Utils.getProblemInstance(size, density, seed1, agent)
            srs = SimpleRandomSearch(state, seed2)
            finalState = srs.doSearch()
        elif algo == algos[1]:
            for each in range(10):
                for each_other in range(10):
                    density = 0.5
                    state = Utils.getProblemInstance(size, density, each, agent)
                    srs = BreadthFirst(state, each_other)
                    finalState = srs.doSearch()
                    piece_data.append(finalState.state.m_agent)
                    size_data.append(finalState.state.m_boardSize)
                    prob_data.append(density)
                    steps_sol.append(len(srs.m_solution))
                    cost_sol.append(srs.m_cost)
                    generated_nodes.append(srs.nGenerated)
                    explored_nodes.append(srs.nVisited)
                    expanded_nodes.append(srs.nExpanded)
        elif algo == algos[2]:
            for each in range(10):
                for each_other in range(10):
                    density = 0.5
                    state = Utils.getProblemInstance(size, density, each, agent)
                    srs = BreadthFirst(state, each_other)
                    finalState = srs.doSearch()
                    piece_data.append(finalState.state.m_agent)
                    size_data.append(finalState.state.m_boardSize)
                    prob_data.append(density)
                    steps_sol.append(len(srs.m_solution))
                    cost_sol.append(srs.m_cost)
                    generated_nodes.append(srs.nGenerated)
                    explored_nodes.append(srs.nVisited)
                    expanded_nodes.append(srs.nExpanded)
        elif algo == algos[3]:
            for each in range(10):
                for each_other in range(10):
                    density = 0.5
                    state = Utils.getProblemInstance(size, density, each, agent)
                    srs = BreadthFirst(state, each_other)
                    finalState = srs.doSearch()
                    piece_data.append(finalState.state.m_agent)
                    size_data.append(finalState.state.m_boardSize)
                    prob_data.append(density)
                    steps_sol.append(len(srs.m_solution))
                    cost_sol.append(srs.m_cost)
                    generated_nodes.append(srs.nGenerated)
                    explored_nodes.append(srs.nVisited)
                    expanded_nodes.append(srs.nExpanded)
        elif algo == algos[4]:
            for each in range(10):
                for each_other in range(10):
                    density = 0.5
                    state = Utils.getProblemInstance(size, density, each, agent)
                    srs = BreadthFirst(state, each_other)
                    finalState = srs.doSearch()
                    piece_data.append(finalState.state.m_agent)
                    size_data.append(finalState.state.m_boardSize)
                    prob_data.append(density)
                    steps_sol.append(len(srs.m_solution))
                    cost_sol.append(srs.m_cost)
                    generated_nodes.append(srs.nGenerated)
                    explored_nodes.append(srs.nVisited)
                    expanded_nodes.append(srs.nExpanded)
        elif algo == algos[5]:
            for each in range(10):
                for each_other in range(10):
                    density = 0.5
                    state = Utils.getProblemInstance(size, density, each, agent)
                    srs = BreadthFirst(state, each_other)
                    finalState = srs.doSearch()
                    piece_data.append(finalState.state.m_agent)
                    size_data.append(finalState.state.m_boardSize)
                    prob_data.append(density)
                    steps_sol.append(len(srs.m_solution))
                    cost_sol.append(srs.m_cost)
                    generated_nodes.append(srs.nGenerated)
                    explored_nodes.append(srs.nVisited)
                    expanded_nodes.append(srs.nExpanded)


    df = pandas.DataFrame({"Piece(nr)": piece_data,
                           "Size(board)": size_data,
                           "Density": prob_data,
                           "Steps(solution)": steps_sol,
                           "Cost(solution)": cost_sol,
                           "Generated nodes": generated_nodes,
                           "Explored nodes": explored_nodes,
                           "Expanded nodes": expanded_nodes})

    df.to_csv('dataframe.csv', index=True, header=True)
