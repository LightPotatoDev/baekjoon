E = []

def expect(a,b):
    n = (b)*(b+1)//2 - (a)*(a-1)//2
    return n / (b-a+1)

for _ in range(2):
    a1,b1,a2,b2 = map(int,input().split())
    E.append(expect(a1,b1) + expect(a2,b2))

if E[0] > E[1]:
    print("Gunnar")
elif E[0] == E[1]:
    print("Tie")
else:
    print("Emma")