#snakes and ladders are played on a 10x10 grid 
#landing on snakes pulls you back n spaces 
#landing on ladders pushes you forward n spaces
#find the least number of turns it takes to play snakes and ladders
#given one six-sided die to play with...
#squares on the grid are in the range of square 1 - square 100.


#Because the 10x10 grid is contiguous, we can imagine this as an array of 100 elements
#elements representing snakes or ladders will contain pointers to transport the player

# these are the squares representing snakes and ladders and their outcomes:
#snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
#ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

from dictionaries import Dict
import random

#function that throws a 6-sided die
def throwdice(): 
    val = random.randrange(5) + 1
    return val


snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

board = {}
position = 1
num_moves = 0
moves_arr = []
i = 1
#Creates the board dictionary with the snakes and ladders values. Negative values for snake indicies and 
#positive values for ladder indices and 0's for neutral indicies.

while i != 101:
  board[i] = 0 #sets a default value for all keys first
  if i in snakes: #searches for key value in snakes 
      val = -1 * snakes[i]
      board[i] = val
  if i in ladders: #searches for key value in ladders
      board[i] = ladders[i]
  i += 1 

for j in range(100000):
    position = 1
    num_moves = 0
    while position != 100: #plays game until player position is 100
        move = throwdice()
        num_moves += 1
        position += move

        if position > 100: #nulls the roll if the die shoots past the 100th square
            position -= move
            num_moves -= 1
            continue

        #checks if the player position is on a snake or a ladder
        val = board[position] 
        if val < 0:
            position += val
        if val > 0: 
            position = val

        if position == 100:
            moves_arr.append(num_moves)

#print(moves_arr)
moves_arr.sort()
#print(moves_arr)
print(moves_arr[0]) 
print(moves_arr[-1])


