X = []
Y = []

for _ in range(3):
    a, b = map(int,input().split())
    X.append(a)
    Y.append(b)

x_4th = [i for i in X if X.count(i) == 1][0]
y_4th = [i for i in Y if Y.count(i) == 1][0]

print(x_4th,y_4th)