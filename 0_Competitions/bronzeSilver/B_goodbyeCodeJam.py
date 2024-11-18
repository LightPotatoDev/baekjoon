import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    Cutline = [4500,1000,25]
    res = "World Finals"

    for i in range(3):
        if n > Cutline[i]:
            res = "Round " + str(i+1)
            break

    print(f"Case #{tc}: {res}")