n = int(input())
S = {input() for _ in range(n)}
S = list(S)
S.sort(key=lambda x:(len(x),x))

for i in S:
    print(i)