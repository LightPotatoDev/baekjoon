n = int(input())

X = [0]*n
Y = [0]*n

for i in range(n):
    X[i], Y[i] = map(int, input().split())

print((max(X)-min(X)) * (max(Y)-min(Y)))