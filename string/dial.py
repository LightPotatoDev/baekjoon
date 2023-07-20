alphaGroup = ("ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ")
s = input()
time = 0

def grouping(letter):
    for i in range(8):
        if letter in alphaGroup[i]:
            return i+3

for i in s:
    time += grouping(i)

print(time)