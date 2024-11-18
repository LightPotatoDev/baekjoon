class Person:
    def __init__(self,p,g):
        self.pos = p
        self.gender = g
        self.coupled = 0

    def __repr__(self):
        return "[" + str(self.pos) + " " + str(self.gender) + " " + str(self.coupled) + "]"

n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
if n > m:
    A,B = B,A

line = []
for i in A:
    line.append(Person(i,1))
for i in B:
    line.append(Person(i,2))
line.sort(key = lambda x:x.pos)
ans = 0

def distance(i,j):
    return abs(line[i].pos - line[j].pos)

def find_couple(idx):
    cpl1 = -1
    cpl2 = -1
    for i in range(idx,-1,-1):
        if line[i].coupled == 0 and line[i].gender == 2:
            cpl1 = i
            break

    for i in range(idx,len(line),1):
        if line[i].coupled == 0 and line[i].gender == 2:
            cpl2 = i
            break

    if cpl1 == -1:
        return cpl2
    elif cpl2 == -1:
        return cpl1
    elif distance(cpl1,idx) <= distance(cpl2,idx):
        return cpl1
    else:
        return cpl2

for i in range(len(line)):
    if line[i].gender == 1:
        j = find_couple(i)
        line[i].coupled = 1
        line[j].coupled = 1
        ans += distance(i,j)

print(ans)