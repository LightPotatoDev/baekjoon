from collections import deque
import sys

n = int(input())
de = deque([])

for _ in range(n):
    command = sys.stdin.readline()

    if "push_back" in command:
        num = int(command.split()[1])
        de.append(num)

    elif "push_front" in command:
        num = int(command.split()[1])
        de.appendleft(num)

    elif command == "pop_front\n":
        try:
            print(de.popleft())
        except:
            print(-1)

    elif command == "pop_back\n":
        try:
            print(de.pop())
        except:
            print(-1)


    elif command == "size\n":
        print(len(de))

    elif command == "empty\n":
        print(int(len(de)==0))

    elif command == "front\n":
        try:
            print(de[0])
        except:
            print(-1)

    elif command == "back\n":
        try:
            print(de[-1])
        except:
            print(-1)