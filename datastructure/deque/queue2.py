from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
de = deque([])

for _ in range(n):
    command = input().rstrip()

    if "push" in command:
        num = int(command.split()[1])
        de.append(num)

    if command == "pop":
        try:
            print(de.popleft())
        except:
            print(-1)

    if command == "size":
        print(len(de))

    if command == "empty":
        print(int(len(de)==0))

    if command == "front":
        try:
            print(de[0])
        except:
            print(-1)

    if command == "back":
        try:
            print(de[-1])
        except:
            print(-1)