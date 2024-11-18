import sys
input = sys.stdin.readline

q = int(input())
webs = []

class Website:
    def __init__(self):
        self.books = set()
        self.min_price = int(1e9)
        self.max_price = 0

    def add(self,price):
        books.add(price)
        self.min_price = min(self.min_price,price)
        self.max_price = max(self.max_price,price)

    def remove(self,price):
        if not (price in books):
            return
        books.remove(price)
        if len(books) == 0:
            del self

for _ in range(q):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        price = cmd[1]
        idx = 0
        for w in webs:
            if w.max_price*2 <= price:
                idx += 1
ldsafj;rej;gnwer;fiwj
