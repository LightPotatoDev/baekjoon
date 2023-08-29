import sys
input = sys.stdin.readline

s = input().rstrip()
bin = ("000","001","010","011","100","101","110","111")
L = []

for i in s:
    L.append(bin[int(i)])
print(int(''.join(L)))