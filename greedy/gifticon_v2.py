import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
gifts = [[A[i],B[i]] for i in range(n)]
gifts.sort(key = lambda x:(x[1],x[0]))
ans = 0

class GiftSet:
    def __init__(self):
        self.L = []
        self.min_date = 0
        self.max_date = 0

    def calc_minmax(self):
        self.min_date = min([self.L[i][0] for i in range(len(self.L))])
        self.max_date = max([self.L[i][0] for i in range(len(self.L))])

    def extend_date(self,cut):
        cut = max(cut,self.L[0][1])
        times = 0
        for i in range(len(self.L)):
            ext = 0
            if (self.L[i][0] < cut):
                ext = (cut-self.L[i][0]-1) // 30 + 1
            self.L[i][0] += 30*ext
            times += ext

        return times

    def append(self,g):
        self.L.append(g)

    def __repr__(self):
        s = str(self.L) + " min = " + str(self.min_date) + " max = " + str(self.max_date) + '\n'
        return s

giftset = [GiftSet()]
giftset[0].append(gifts[0])
for i in range(1,n):
    a,b = gifts[i]
    pa,pb = gifts[i-1]
    if b != pb:
        giftset.append(GiftSet())
    giftset[-1].append([a,b])

cut = 0
ans = 0
for g in giftset:
    ans += g.extend_date(cut)
    g.calc_minmax()
    cut = g.max_date

print(ans)