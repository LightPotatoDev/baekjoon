import sys
input = sys.stdin.readline

n = int(input())
BOJ = []
Others = []

for _ in range(n):
    rec = input().rstrip()
    if len(rec) >= 8 and rec[:7] == "boj.kr/":
        BOJ.append(rec)
    else:
        Others.append(rec)

Others.sort(key = lambda x:(len(x), x))
BOJ.sort(key = lambda x:(int(x[7:])))
for i in Others:
    print(i)
for i in BOJ:
    print(i)