class Paper:
    def __init__(self,two,one):
        self.twos = two
        self.ones = one

    def paste(self,mode,num):
        pasting = 0

        if mode == 2:
            pasting = min(self.twos,num)
            self.twos -= pasting
            self.ones -= pasting*4

        if mode == 1:
            pasting = min(self.ones,num)
            self.ones -= pasting

        return num - pasting

L = [0]+[int(input()) for _ in range(6)]
papers = []

for _ in range(L[6]):
    papers.append(Paper(0,0))
for _ in range(L[5]):
    papers.append(Paper(0,11))
for _ in range(L[4]):
    papers.append(Paper(5,20))
for _ in range(L[3]//4):
    papers.append(Paper(0,0))
if L[3] % 4 == 1:
    papers.append(Paper(5,27))
if L[3] % 4 == 2:
    papers.append(Paper(3,18))
if L[3] % 4 == 3:
    papers.append(Paper(1,9))

for p in papers:
    L[2] = p.paste(2,L[2])
for _ in range(L[2]//9):
    papers.append(Paper(0,0))
if L[2]%9 != 0:
    papers.append(Paper(9-L[2]%9,36-(L[2]%9)*4))

for p in papers:
    L[1] = p.paste(1,L[1])
for _ in range(L[1]//36):
    papers.append(Paper(0,0))
if L[1]%36 != 0:
    papers.append(Paper(0,1))

print(len(papers))
