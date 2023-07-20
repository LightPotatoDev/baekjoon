n = int(input())
chessboard = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0

def placeable(queens,y,x):

    cant = set()

    for q in queens:
        for i in range(n):
            cant.add((q[0],i)) #가로
            cant.add((i,q[1])) #세로

        i = q[0] - min([q[0],q[1]])
        j = q[1] - min([q[0],q[1]])
        while i < n-1 and j < n-1:
            i += 1
            j += 1 #오른쪽 아래 대각선
            cant.add((i,j))

        i = q[0] - min([q[0],n-q[1]-1])
        j = q[1] + min([q[0],n-q[1]-1])
        while i < n-1 and j > 0:
            i += 1
            j -= 1 #왼쪽 아래 대각선
            cant.add((i,j))

    if (y,x) in cant:
        return False
    else:
        return True

def placequeen(queens,place):
    global cnt

    if len(queens) >= n:
        cnt += 1
        return
    elif place >= n**2:
        return

    spot = [place//n,place%n]

    if placeable(queens,spot[0],spot[1]):
        placequeen(queens + [spot],place+1) #퀸을 배치하는 경우

    placequeen(queens,place+1) #퀸을 배치하지 않는 경우

placequeen([],0)
print(cnt)