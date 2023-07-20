import sys

n = int(input())
L = []

for _ in range(n):
    command = sys.stdin.readline()

    if "push" in command:
        num = int(command.split()[1])
        L.append(num)

    elif command == "pop\n":
        try:
            print(L.pop(-1))
        except:
            print(-1)

    elif command == "size\n":
        print(len(L))

    elif command == "empty\n":
        print(int(len(L)==0))

    elif command == "top\n":
        try:
            print(L[-1])
        except:
            print(-1)