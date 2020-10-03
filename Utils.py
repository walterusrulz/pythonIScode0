#import java.text.DecimalFormat;
#import java.util.ArrayList;
#import java.util.Random;

import sys
import random
from Position import Position
from State import State


# all the pieces
wPawn = 0
wRook = 1
wBishop = 2
wKnight = 3 # 33?
wQueen = 4
wKing = 5
bPawn = 6
bRook = 7
bBishop = 8
bKnight = 9
bQueen = 10
bKing = 11
empty = 12

# number of pieces
diffPieces = 12
numPieces = [8,2,2,2,1,1,8,2,2,2,1,1]

# name (and letter) of each piece
names = ["wPawn", "wRook", "wBishop", "wkNnight", "wQueen", "wKing", "bPawn", "bRook", "bBishop", "bkNightight", "bQueen", "bKing"]
letters = ["P","R","B","N","Q","K","p","r","b","n","q","k"," "]
# Note we use h for Horse instead of Knight
# Note we add " " for empty cell

# Get color piece
def getColorPiece(piece):

    if ((piece >=0) and (piece<=5)):
    	return 0 #white
    elif ((piece>5) and (piece<=11)):
    	return 1 #black
    else:
    	print("\n** Error, wrong piece code\n")
    	sys.exit(0)
    return -1  #never arrives here, just to avoid compilation error


# This method generates a problem instance.
# @param n size of the board
# @param p probability for each piece to be included
# @param seed to initiate the random generator (for reproducibility)
# @param agent the type of piece who will "play" the game (always white)
# @return the initial state (board and agent)

def getProblemInstance(n, p, seed, agent):
   board = [[empty for i in range(n)] for j in range(n)]
   # a board of NxN dimensions, filled with 12-s representing empty, comprehension list?
   random.seed(seed)
   # discounts one piece of the agent type
   numPieces[agent] -= 1
   # a list of all positions, by row and incrementally
   allPositions = getAllBoardPositions(n)

   # placing our agent in the first row, we know these are the first n elements in allPositions
   r = random.randint(0,n-1)
   # will return random between 0 and last postion of 1st row, meaning starting from the top of the screen
   agentPos = allPositions.pop(r)
   # pop the Position form the Alist, and use it as an index to place the agent
   board[agentPos.row][agentPos.col] = agent
		
   # placing the rest of pieces
   pos = None
   # First, iterate through all the 12 (2 x 6) figures, and within each, place as much
   # unit of the same (minus the agent we discounted) on the board, popping Positions
   # Cannot see that it treats different colours in a specific way
   for piece in range(diffPieces):
      for j in range(numPieces[piece]):
      	if (random.random()<=p):
      		r = random.randint(0,len(allPositions)-1)
      		pos = allPositions.pop(r)
      		board[pos.row][pos.col] = piece
		
   # Creating the instance, i.e., the state
   # Returning fully (as much as Probability p permits) populated board, position of ur agent,
   # which we randomly got, although knowingly on first row, and type, chosen by us
   return State(board, agentPos, agent)



#
# fill (by rows) an ArrayList with all the possible coordinates
# 
# @param n size of the board
#
# This is just to get a full list of Positions to pop when assigning pieces
def getAllBoardPositions(n):
	return [Position(r,c) for r in range(n) for c in range(n)]
	

#
# Print a state (board + agent)
#
# Printer, not fully revised
def printBoard(state):
	#DecimalFormat df = new DecimalFormat("00");
	size = len(state.m_board[0])
	if (size>50):
		print("**Error, board too large to be text-printed ...\n")
		sys.exit(0)

	# upper row
	print("   ", end="")
	for c in range(size):
		print("% 2d " % (c), end="")
	print("")

	print("  ", end="")
	for c in range(size):
		print("---", end="")
	print("--")

	# board
	for r in range(size):
		print("% 2d|" % (r), end="")
		for c in range(size): 
			if ((r==state.m_agentPos.row) and (c==state.m_agentPos.col)):
				print("*" + letters[state.m_board[r][c]]+"|", end="")
			else:
				print(" " + letters[state.m_board[r][c]]+"|", end="")
		# botton row
		print("  ")
		for c in range(size): 
			print("---", end="")
		print("--")


def getPossibleMoves(state):
	legalMovesList = []
	actPos = Position(state.m_agentPos.row, state.m_agentPos.col)
	nextPos = actPos.copy()
	if state.m_agent == 0:
		while state.m_board[nextPos.row][nextPos.col] not in range(5, 12) and not nextPos.col == len(state.m_board[0]):
			nextPos.row += 1
			addedPos = nextPos.copy()
			legalMovesList.append(addedPos)
		print("Not implemented")
	elif state.m_agent == 1:
		print("Not implemented")
	return legalMovesList

# main to test the methods

if __name__ == '__main__':

	st = getProblemInstance(8, 1.0, 1771, wRook)
	print(st.m_board)
		
	printBoard(st)
