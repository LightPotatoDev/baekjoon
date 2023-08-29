board = list(input())

i = 0
while i < len(board):
    if board[i] == "X":
        if board[i:i+4] == list("X"*4):
            board[i:i+4] = list("A"*4)
            i += 4
        elif board[i:i+2] == list("X"*2):
            board[i:i+2] = list("B"*2)
            i += 2
        else:
            print(-1)
            exit(0)
    else:
        i += 1

print(''.join(board))

"""
by tlswlgns777
board=board.replace("XXXX","AAAA")
board=board.replace("XX","BB")

if 'X' in board:
    print(-1)

else:
    print(board)
"""