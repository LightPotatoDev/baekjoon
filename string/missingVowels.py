s = input()
f = input()
vowels = {'a','e','i','o','u','y'}
s = s.lower()
f = f.lower()

SC = []
SV = []

FC = []
FV = []

for i in s:
    if i in vowels:
        SV.append(i)
    else:
        SC.append(i)

for i in f:
    if i in vowels:
        FV.append(i)
    else:
        FC.append(i)

if SC != FC:
    print('Different')
    exit()

cnt = 0
for i in FV:
    if cnt == len(SV):
        break
    if SV[cnt] == i:
        cnt += 1

if cnt == len(SV):
    print('Same')
else:
    print('Different')
