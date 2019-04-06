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
    print("    0    1    2")
    print_row = 0       
    for row in board:
        print(print_row, row)
        print_row+=1 

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
            return True
        if row.count('O') == 3:
            print("Player O Won!")
            return True

    ## Check columns for all of one value
    for index in range(3):
        if column(game_board, index).count('X') == 3:
            print('Player X Won!')
            return True
        if column(game_board, index).count('O') == 3:
            print('Player O Won!')
            return True

    ## Check diagonal for all of one value
    down_left, down_right = diagonal(game_board)
    if down_left.count('X') == 3 or down_right.count('X') == 3:
        print('Player X Won!')
        return True

    if down_left.count('O') == 3 or down_right.count('O') == 3:
        print('Player O Won!')
        return True
    return False

def continue_prompt():
    continue_input=int(input('Do you dare?\nyes(1)  no(2): '))
    while True:  
        if continue_input == 1:
            return True
        elif continue_input == 2:
            return False        
        else:
            continue_input=int(input('Do you dare?\nyes(1)  no(2): '))
            



def reset_game(game_board, player):
    game_board = [['q','q','q'],
                  ['q','q','q'],
                  ['q','q','q']]
    player=players[rand.randint(0,1)]

def main():
    print_board(game_board)
    player=players[rand.randint(0,1)]
    print("Player ", player, " Goes first")
    while True:
        row=int(input('Pick a row any row'))
        column=int(input('Pick a coulmn'))
        move(player, row, column)
        if victory(): 
            if continue_prompt():
                reset_game(game_board, player)
            else:
                break
        if player=='X':
            player='O'
        else:
            player='X'
        
     
        print_board(game_board)
        print("Player ", player, " Goes now")

main()




