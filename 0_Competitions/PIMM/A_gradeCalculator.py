s = input()
D = {"A+":4.5, "A":4, "B+":3.5, "B":3, "C+":2.5, "C":2,
    "D+":1.5, "D":1, "F":0}

L = []
i = 0
while i < len(s):
    if i+1 < len(s) and s[i+1] == "+":
        L.append(s[i]+s[i+1])
        i += 2
    else:
        L.append(s[i])
        i += 1

score = 0
for i in L:
    score += D[i]
print(score / len(L))