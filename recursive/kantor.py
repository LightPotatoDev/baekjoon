def kantor(s,e):
    global theset
    if s+1 < e:
        for i in range(s+(e-s+1)//3,s+2*((e-s+1)//3)):
            theset[i] = ' '

        kantor(s,s+(e-s)//3)
        kantor(s+2*((e-s)//3),e)
    else:
        return


while True:
    try:
        n = int(input())
    except EOFError:
        break

    s = '-'*(3**n)
    theset = list(s)
    kantor(0, 3**n)
    print(''.join(theset))

""" by damin1025
import sys

def cut(a,n):
    if n == 1:
        return
    for i in range(a+n//3, a+(n//3)*2):
        canto[i] = ' '
    cut(a,n//3) # 왼쪽 잘라나가기
    cut(a+n//3*2,n//3) # 오른쪽 잘라나가기


while True:
    try:
        n = int(sys.stdin.readline())
        canto = ['-'] * (3**n)
        cut(0,3**n)
        print(''.join(canto))
    except:
        break

a: starting position
n: length
"""
