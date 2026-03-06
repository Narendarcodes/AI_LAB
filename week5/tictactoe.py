import math

# Tic Tac Toe board
board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_full():
    return " " not in board

def minimax(is_max):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_full():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(score, best)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(score, best)
        return best

def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def play():
    print("Positions are 1-9")
    print_board()

    while True:
        pos = int(input("Your move (1-9): ")) - 1
        if board[pos] == " ":
            board[pos] = "X"
        else:
            print("Invalid move")
            continue

        print_board()

        if check_winner("X"):
            print("You win!")
            break
        if is_full():
            print("Draw!")
            break

        ai_move = best_move()
        board[ai_move] = "O"
        print("AI move:")
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break
        if is_full():
            print("Draw!")
            break

play()