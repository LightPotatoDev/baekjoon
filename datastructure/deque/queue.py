from collections import deque
import sys

n = int(input())
de = deque([])

for _ in range(n):
    command = sys.stdin.readline()

    if "push" in command:
        num = int(command.split()[1])
        de.append(num)

    if command == "pop\n":
        try:
            print(de.popleft())
        except:
            print(-1)

    if command == "size\n":
        print(len(de))

    if command == "empty\n":
        print(int(len(de)==0))

    if command == "front\n":
        try:
            print(de[0])
        except:
            print(-1)

    if command == "back\n":
        try:
            print(de[-1])
        except:
            print(-1)