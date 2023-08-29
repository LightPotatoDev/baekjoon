D = dict()
Tenpai = set()
Ban = set()
Adding = set()

for i in range(1,10):
    for j in ["s","t","m"]:
        D[str(i)+j] = 0
for i in ["e","s","w","n","h","b","j"]:
    D[i] = 0

for i in input().split():
    D[i] += 1

for i in D:
    if D[i] == 4:
        Ban.add(i)

#치또이츠
chito = 0
missing = ""
for i in D:
    if D[i] == 2:
        chito += 1
    if D[i] == 1:
        missing = i
if chito == 6 and missing != "":
    Adding.add(missing)

#국사무쌍
kuk = ["1s","9s","1m","9m","1t","9t","e","s","w","n","h","b","j"]
exist = [0]*13
for i,x in enumerate(kuk):
    if D[x] >= 1:
        exist[i] = D[x]
if exist.count(1) >= 11:
    if exist.count(1) == 13:
        for j in kuk:
            Adding.add(j)
    elif exist.count(2) == 1:
        Adding.add(kuk[exist.index(0)])


#normal
def bodyCheck(i,j):
    for k in range(3):
        if D[str(i+k)+j] == 0:
            return False
    for k in range(3):
        D[str(i+k)+j] -= 1
    return True

def getComb(head,body):
    for i in D:
        if head == 0 and D[i] >= 2:
            D[i] -= 2
            getComb(head+1,body)
            D[i] += 2

        if D[i] >= 3:
            D[i] -= 3
            getComb(head,body+1)
            D[i] += 3

    for i in range(1,8):
        for j in ["s","t","m"]:
            if bodyCheck(i,j):
                getComb(head,body+1)
                for k in range(3):
                    D[str(i+k)+j] += 1

    A = []
    for i in D:
        if D[i] > 0:
            for _ in range(D[i]):
                A.append(i)
    if len(A) <= 2:
        B = tuple(A)
        Tenpai.add(B)

getComb(0,0)

def addMissingNumber(alp,n1,n2):
    if n2 - n1 == 1:
        if n1 >= 2:
            Adding.add(str(n1-1)+alp)
        if n2 <= 8:
            Adding.add(str(n2+1)+alp)
    elif n2 - n1 == 2:
        Adding.add(str(n1+1)+alp)

for Left in Tenpai:
    if len(Left) == 1:
        Adding.add(Left[0])
    else:
        if Left[0] == Left[1]:
            Adding.add(Left[0])
        elif len(Left[0]) == 2 and len(Left[1]) == 2:
            Left = sorted(list(Left))
            num1, num2 = int(Left[0][0]), int(Left[1][0])
            alpha1, alpha2 = Left[0][1], Left[1][1]
            if alpha1 == alpha2:
                addMissingNumber(alpha1,num1,num2)

ans = list(Adding-Ban)
ans.sort()

if ans:
    print("tenpai")
    print(len(ans))
    print(*ans)
else:
    print("no tenpai")