import sys
input = sys.stdin.readline

T = int(input())

def compare(x,i):
    for j in range(i+1,11):
        for


for _ in range(T):
    L = [[] for _ in range(11)]
    n = int(input())
    for _ in range(n):
        s = input()
        L[len(s)].append(s)

    for i in range(1,10):
        for x in L[i]:
            compare(x,i)