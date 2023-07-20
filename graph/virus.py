coms = int(input())
n = int(input())
relations = []
infected = [0]*(coms+1)
infected[1] = 1

for _ in range(n):
    x, y = map(int,input().split())
    relations.append([x,y])
    relations.append([y,x])

checklist = [1]
while len(checklist) > 0:
    for j in relations:
        if j[0] == checklist[0] and infected[j[1]] == 0:
            infected[j[1]] = 1
            checklist.append(j[1])
    checklist.pop(0)

print(sum(infected)-1)