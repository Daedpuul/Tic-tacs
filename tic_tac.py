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
        if row.count('Y') == 3:
            print("Player Y Won!")

    ## Check columns for all of one value
    for index in range(2):
        if column(game_board, index).count('X') == 3:
            print('Player X Won!')
        if column(game_board, index).count('Y') == 3:
            print('Player Y Won!')

    ## Check diagonal for all of one value
    down_left, down_right = diagonal(game_board)
    if down_left.count('X') == 3 or down_right.count('X') == 3:
        print('Player X Won!')

     if down_left.count('Y') == 3 or down_right.count('y') == 3:
        print('Player Y Won!')



move('X', 0, 0)
move('X', 1, 0)
move('X', 2, 0)
print_board(game_board)
victory()


