lines = [6,2,5,5,4,5,6,3,7,5]
dp = [[-1]*106 for _ in range(16)]
INF = int(1e20)
for j,x in enumerate([1,7,4,2,0,8]):
    dp[1][j+2] = str(x)

def find_lowest(i,j):
    c1 = [dp[1][k] for k in range(2,8)]
    c2 = [dp[i-1][k] for k in range((i-1)*2, (i-1)*7+1)]
    res = INF
    for i1,s1 in enumerate(c1):
        for i2,s2 in enumerate(c2):
            if i1+i2+2+(i-1)*2 != j:
                continue
            s_list = list(s1+s2)
            s_list.sort()
            s = ''.join(s_list)
            if int(s) < int(res):
                res = s

    return res

for i in range(2,16):
    for j in range(i*2, i*7+1):
        dp[i][j] = find_lowest(i,j)

def solve(n_str):
    n_len = len(n_str)
    n = int(n_str)
    ans = 10**n_len

    def get_lines(s):
        if s == -1:
            return 0
        line_num = 0
        for i in s:
            line_num += lines[int(i)]
        return line_num

    def make_new_number(n_str,i,j,k):
        n_list = list(n_str)
        n_list[n_len-i-1] = str(j)
        for l in range(i):
            n_list[n_len-i+l] = dp[i][k][l]

        return int(''.join(n_list))

    for i in range(n_len):
        for j in range(10):
            for k in range(i*2, i*7+1):
                if get_lines(n_str[::-1][:i+1]) == get_lines(str(j)) + get_lines(dp[i][k]):
                    new = make_new_number(n_str,i,j,k)
                    new_ans = new-n
                    if new_ans > 0:
                        ans = min(ans, new_ans)
                    elif new_ans < 0:
                        ans = min(ans, new_ans + 10**n_len)

    return ans

n_str = input()
print(solve(n_str))

counted = []
for i in range(10000):
    n = str(i).zfill(4)
    counted.append(solve(n))

import pickle

with open('dp_count_to_10000.pickle','wb') as fw:
    pickle.dump(counted,fw)
