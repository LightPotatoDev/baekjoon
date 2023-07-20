T = int(input())

for _ in range(T):
    repeated = ""
    r, s = input().split()
    for i in s:
        repeated += i * int(r)
    print(repeated)