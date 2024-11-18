s = input()
t = input()

bList = []
b = 0
for i in t:
    if i == 'B':
        b += 1
    bList.append(b)

sB = s.count('B')
tB = t.count('B')
if (tB - sB) % 2 == 1:
    s = s[::-1]

def search(i):
    for j in range(len(s)):
        if s[j] != t[i+j]:
            return False
    return True

for i in range(len(t)-len(s)+1):
    if search(i):
        bLeft = bList[i-1] * int(i > 0)
        bRight = bList[-1] - bList[i+len(s)-1]

        if 0 <= bRight - bLeft <= 1:
            flag = True
            if (tB - sB) % 2 == 1 and bRight == 0 and i != len(t)-len(s) and t[-1] == 'A':
                flag = False
            if (tB - sB) % 2 == 0 and bLeft == 0 and i != 0 and t[0] == 'A':
                flag = False
            if flag == True:
                print(1)
                exit()

print(0)
