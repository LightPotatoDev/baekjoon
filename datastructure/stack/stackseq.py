import sys

n = int(input())
L = [int(sys.stdin.readline()) for _ in range(n)]

mode = "+"
stack = []
pushed = 0
count = 1

output = []
while count <= n:
    if mode == "+":
        output.append("+")
        stack.append(count)
        if L[pushed] == stack[-1]:
            mode = "-"
        else:
            count += 1

    if mode == "-":
        output.append("-")
        pushed += 1
        stack.pop(-1)
        if len(stack) == 0 or L[pushed] != stack[-1]:
            mode = "+"
            count += 1

if stack[::-1] == L[pushed:]:
    output += ["-"] * (n-pushed)
    for i in output:
        print(i)
else:
    print("NO")

"""
딴사람이 만듦
import sys

n = int(sys.stdin.readline())
stack = []
res = []
flag = 0
e = 1

for i in range(n) :
    req = int(sys.stdin.readline())

    while e <= req :
        stack.append(e)
        res.append("+")
        e += 1
    if stack[-1] == req :
        stack.pop()
        res.append("-")
    else :
        print("NO")
        flag = 1
        break

if flag == 0 :
    for i in res :
        print(i)
"""