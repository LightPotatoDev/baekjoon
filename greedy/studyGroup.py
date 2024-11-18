class Student:
    def __init__(self,skill,algo):
        self.skill = skill
        self.algo = algo

    def __repr__(self):
        return str(self.skill) + str(self.algo)

n,k,d = map(int,input().split())
students = []
for _ in range(n):
    m,sk = map(int,input().split())
    stud = Student(sk,list(map(lambda x:int(x)-1,input().split())))
    students.append(stud)

students.sort(key = lambda x : x.skill)

i = 0
j = 0
knows = [0]*k
ans = 0

for a in students[0].algo:
    knows[a] += 1
while i < n-1:
    skill_diff = students[j].skill - students[i].skill
    if skill_diff <= d:
        group_num = j-i+1
        someone_knows = sum([int(knows[t] > 0) for t in range(k)])
        everyone_knows = sum([int(knows[t] == group_num) for t in range(k)])
        ans = max(ans, (someone_knows - everyone_knows) * group_num)

    if skill_diff <= d and j < n-1:
        j += 1
        for a in students[j].algo:
            knows[a] += 1
    else:
        for a in students[i].algo:
            knows[a] -= 1
        i += 1

print(ans)