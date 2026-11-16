#Minimax algorithm (Tic-Tac-Toe Game)
N = 9
board = [' ']*N

def winner():
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a,b,c in wins:
        if(board[a] == board[b] == board[c] != ' '):
            return board[a]
    return None


def minimax(max_player):
    if winner() == 'X':
        return 1
    if winner() == 'O':
        return -1
    if ' ' not in board:
        return 0
    if max_player:
        best = -999
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = 999
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(True))
                board[i] = ' '
        return best

def computer():
    best = -999
    move = 0

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(False)
            board[i] = ' '

            if (score > best):
                best = score
                move = i
    board[move] = 'X'   

while True:
    computer()

    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])

    if winner() == 'X':
        print("Computer wins!!")
        break
    if ' ' not in board:
        print("Draw")
        break

    pos = int(input("Enter position (1-9): ")) - 1
    if pos < 0 or pos > 8 or board[pos] != ' ':
        print("Invalid move!!")
        continue
    
    board[pos] = 'O'

    if winner() == 'O':
        print("You win!!")
        break