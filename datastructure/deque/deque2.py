from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
de = deque([])

for _ in range(n):
    cmd = input().rstrip()

    if cmd[0] == "1":
        num = int(cmd.split()[1])
        de.appendleft(num)

    elif cmd[0] == "2":
        num = int(cmd.split()[1])
        de.append(num)

    elif cmd == "3":
        if de:
            print(de.popleft())
        else:
            print(-1)

    elif cmd == "4":
        if de:
            print(de.pop())
        else:
            print(-1)

    elif cmd == "5":
        print(len(de))

    elif cmd == "6":
        print(int(len(de)==0))

    elif cmd == "7":
        if de:
            print(de[0])
        else:
            print(-1)

    elif cmd == "8":
        if de:
            print(de[-1])
        else:
            print(-1)