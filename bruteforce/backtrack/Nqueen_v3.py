n = int(input())
cnt = 0

def placeable(queens,y,x):
    for q in queens:
        if y == q[0]: return False #세로
        if x == q[1]: return False #가로
        if y-x == q[0]-q[1]: return False #오른쪽 아래 대각선
        if y+x == q[0]+q[1]: return False #왼쪽 아래 대각선

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
        placequeen(queens + [spot],place+(n-place%n)) #퀸을 배치하는 경우

    placequeen(queens,place+1) #퀸을 배치하지 않는 경우

placequeen([],0)
print(cnt)