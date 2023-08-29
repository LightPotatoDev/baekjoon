import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
S = A[:]
for i in range(n-1):
    S[i+1] += S[i]

score = 0
turn = 0 #0:first, 1:second
while n > 0:

    shot = False
    for i in range(n):
        sD = S[n-1]-S[i]
        sU = S[i-1] * int(i!=0)
        if (A[i] > sD or (A[i]==sD and i==0)) and A[i]+sU > 0:
            if turn == 0:
                score += A[i]
            else:
                score += sD*int(n!=0)
            n -= (n-i)
            shot = True
            break
    if shot == False:
        if turn == 1:
            score += S[n-1]*int(n!=0)
        break

    turn = not turn

print(score)