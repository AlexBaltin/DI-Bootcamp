def welcome():
    print("Welcome to TIC TAC TOE!")


def display_board(values):

    print("\n")

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0][0], values[0][1], values[0][2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[1][0], values[1][1], values[1][2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[2][0], values[2][1], values[2][2]))
    print("\t     |     |")
    
    print("\n")


def player_input(player):
    print(f"Player {player}'s turn ...")
    row = input("Enter row: ")
    col = input("Enter column: ")
    return int(row), int(col)


def check_win(values):
    for y in range(3):
        if values[y][0] == values[y][1] and values[y][1] == values[y][2]:
            return True
    
    for x in range(3):
        if values[0][x] == values[1][x] and values[1][x] == values[2][x]:
            return True
        
    if values[0][0] == values[1][1] and values[1][1] == values[2][2]:
        return True
    
    if values[0][2] == values[1][1] and values[1][1] == values[2][0]:
        return True

    else: 
        return False




welcome()
values = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
is_finished = False
current_player = "X"

while is_finished is False:
    display_board(values)
    row, col = player_input(current_player)
    
    # if ... is_empty:
    values[row - 1][col - 1] = current_player

    is_win = check_win(values)
    is_full = False
    
    is_finished = False  # is_win or is_full
    
    if current_player == "X":
        current_player = "O"
        continue
    
    if current_player == "O":
        current_player = "X"
        continue

print("Game finished!!")