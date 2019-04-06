import random as rand
players= ['X','O']
game_board = [['q','q','q'],
              ['q','q','q'],
              ['q','q','q']]

def move(player, row, column):
    if game_board[row][column] == 'q':
        game_board[row][column] = player
    else:
        print("invalid location")

def print_board(board):
    for row in board:
        print(row)

def column(array, index):
    return [row[index] for row in array]

def diagonal(array):
    down_left_inside_function = [game_board[0][0], game_board[1][1], game_board[2][2]]
    down_right_inside_function = [game_board[0][2], game_board[1][1], game_board[2][0]]
    print("Down_left", down_left_inside_function)
    print("Down_right", down_right_inside_function)
    return down_left_inside_function, down_right_inside_function

def victory():
    ## Check rows for all one value
    for row in game_board:
        # row = ['q', 'q', 'q']
        if row.count('X') == 3:
            print("Player X Won!")
        if row.count('O') == 3:
            print("Player O Won!")

    ## Check columns for all of one value
    for index in range(2):
        if column(game_board, index).count('X') == 3:
            print('Player X Won!')
        if column(game_board, index).count('O') == 3:
            print('Player O Won!')

    ## Check diagonal for all of one value
    down_left, down_right = diagonal(game_board)
    if down_left.count('X') == 3 or down_right.count('X') == 3:
        print('Player X Won!')

    if down_left.count('O') == 3 or down_right.count('O') == 3:
        print('Player O Won!')






def main():
    print_board(game_board)
    player=players[rand.randint(0,1)]
    print("Player ", player, " Goes first")
    while True:
        row=int(input('Pick a row any row'))
        column=int(input('Pick a coulmn'))
        move(player, row, column)
        if player=='X':
            player='O'
        else:
            player='X'
        
     
        print_board(game_board)
        print("Player ", player, " Goes now")

main()




