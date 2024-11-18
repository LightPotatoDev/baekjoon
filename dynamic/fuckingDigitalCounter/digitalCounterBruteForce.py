lines = [6,2,5,5,4,5,6,3,7,5]
ITER = 10000

def count_lines(n):
    res = 0
    for s in n:
        res += lines[int(s)]
    return res

def find_ans(n):
    ptr = n
    for i in range(ITER):
        ptr = (ptr + 1) % ITER
        if counted[n] == counted[ptr]:
            return i+1

counted = []

for i in range(ITER):
    n = str(i).zfill(4)
    counted.append(count_lines(n))

ans = []
for i in range(ITER):
    ans.append(find_ans(i))

import pickle

with open('bf_count_to_10000.pickle','wb') as fw:
    pickle.dump(ans,fw)