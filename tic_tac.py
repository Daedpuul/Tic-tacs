array = [0,1,2,12,5]
game_board = [['q','q','q'],
              ['q','q','q'],
              ['q','q','q']]

def move(player, row, column):
    game_board[row][column] = player

move('X',0,0)
move('Y',0,0)
print(game_board)

def print_index_times2(array,index ):
    print(array[index] * 2)
print_index_times2(array,2)
def print_by_value(array,value):
    print(array[array.index(value)])
print_by_value(array,5)

# Hey Isaac!


