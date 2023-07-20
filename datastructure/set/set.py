import sys

m = int(input())
S = set()
for _ in range(m):
    command = list(sys.stdin.readline().split())
    if len(command) == 2:
        x = int(command[1])

    if command[0] == 'add':
        S.add(x)

    elif command[0] == 'remove':
        if x in S:
            S.remove(x)

    elif command[0] == 'check':
        print(int(x in S))

    elif command[0] == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)

    elif command[0] == 'all':
        S = {i for i in range(1,21)}

    elif command[0] == 'empty':
        S = set()