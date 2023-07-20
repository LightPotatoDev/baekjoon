a,b,c = map(int,input().split())
remains = []

firsta = a % c
a = firsta
for _ in range(b):
    remains.append(a)
    a = (a * firsta) % c
    if len(remains) >= 2 and remains[-1] == remains[0]:
        remains.pop()
        break

print(remains[b%len(remains)-1])