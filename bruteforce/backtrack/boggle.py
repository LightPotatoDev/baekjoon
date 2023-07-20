import sys
input = sys.stdin.readline

w = int(input())
words = []

for _ in range(w):
    words.append(input().rstrip())
input()

b = int(input())
dx = [-1, 0, 1,-1, 1,-1, 0, 1]
dy = [-1,-1,-1, 0, 0, 1, 1, 1]
flag = False

def game(board, word):
    def boggle(index,y,x,path):

        global flag
        if flag == True:
            return

        if index == len(word):
            flag = True
            possibles.append(word)
            return True

        for i in range(8):
            checkY = y + dy[i]
            checkX = x + dx[i]
            if (0 <= checkY <= 3) and (0 <= checkX <= 3):
                if board[checkY][checkX] == word[index]:
                    if path[checkY][checkX] == 0:
                        path[checkY][checkX] = 1
                        boggle(index+1,checkY,checkX,path)
                        path[checkY][checkX] = 0

        return False

    def bogglestart():
        for i in range(4):
            for j in range(4):
                if board[i][j] == word[0]:
                    path = [[0]*4 for _ in range(4)]
                    path[i][j] = 1
                    boggle(1,i,j,path)

    bogglestart()

for _ in range(b):

    #play game
    board = []
    possibles = []

    for _ in range(4):
        board.append(list(input().rstrip()))

    for word in words:
        game(board,word)
        flag = False
    input()

    #process results
    possibles.sort(key = lambda x:(-len(x), x))
    scorerange = [0,0,0,1,1,2,3,5,11]
    score = 0
    for word in possibles:
        score += scorerange[len(word)]

    print(score, possibles[0], len(possibles))