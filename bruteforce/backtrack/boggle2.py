import sys
input = sys.stdin.readline

w = int(input())
words = []

for _ in range(w):
    word = input().rstrip()
    if 'q' in word and 'qu' not in word:
        continue
    word = word.replace('qu','q')
    words.append(word)

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
            if (0 <= checkY <= d-1) and (0 <= checkX <= d-1):
                if board[checkY][checkX] == word[index]:
                    if path[checkY][checkX] == 0:
                        path[checkY][checkX] = 1
                        boggle(index+1,checkY,checkX,path)
                        path[checkY][checkX] = 0

        return False

    def bogglestart():
        for i in range(d):
            for j in range(d):
                if board[i][j] == word[0]:
                    path = [[0]*d for _ in range(d)]
                    path[i][j] = 1
                    boggle(1,i,j,path)

    bogglestart()

while True:

    #play game
    d = int(input())
    if d == 0: break

    board = []
    possibles = []

    for _ in range(d):
        board.append(list(input().rstrip()))

    for word in words:
        game(board,word)
        flag = False

    #process results
    possibles.sort()
    for word in possibles:
        word = word.replace('q','qu')
        print(word)

    print('-')