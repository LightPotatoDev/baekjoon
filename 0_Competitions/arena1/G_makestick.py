n = int(input())
Stick = list(map(int,input().split()))
#q = int(input())
#Req = list(map(int,input().split()))
Div = [set() for _ in range(100001)]
def divisor(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            Div[n].add(i)
            Div[n].add(n//i)

for i in range(100001):
    divisor(i)

L = [0] * 100001
for i in Stick:
    L[i] = sum([L[j] for j in Div[i]]) + 1

print(Div[:100])
print(L[:100])
