import sys
input = sys.stdin.readline

s = input().rstrip()
S = set()
for i in range(len(s)):
    for j in range(0,len(s)-i):
        S.add(s[j:j+i+1])
print(len(S))