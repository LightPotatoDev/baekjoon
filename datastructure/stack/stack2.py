import sys
input = sys.stdin.readline

n = int(input())
L = []

for _ in range(n):
    cmd = input().rstrip()

    if cmd[0] == "1":
        c,x = map(int,cmd.split())
        L.append(x)
    elif cmd == "2":
        if L:
            print(L.pop())
        else:
            print(-1)
    elif cmd == "3":
        print(len(L))
    elif cmd == "4":
        print(int(len(L)==0))
    elif cmd == "5":
        if L:
            print(L[-1])
        else:
            print(-1)
