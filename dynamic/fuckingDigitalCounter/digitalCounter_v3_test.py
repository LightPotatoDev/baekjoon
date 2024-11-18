lines = [6,2,5,5,4,5,6,3,7,5]
diff = [[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        diff[i][j] = lines[j]-lines[i]

def solve(n_str):
    n = int(n_str)
    n_l = len(n_str)
    one_or_eight = 0

    while (n % 100 == 11 or n % 100 == 88) and n_l >= 3:
        one_or_eight += 1
        n //= 100
        n_str = n_str[:-2]

    l = len(n_str)
    print(n_str)

    delta_cost_incr = []
    delta_cost_decr = []

    for i in range(l):
        incr = []
        decr = []
        num = int(n_str[l-i-1])
        for j in range(10):
            cost = (j-num) * 10**i
            incr.append((j*10**i,diff[num][j], cost))
            if i == l-1 and cost <= 0:
                cost += 10**l
            decr.append((j*10**i,diff[num][j], cost))
        delta_cost_incr.append(incr)
        delta_cost_decr.append(decr)

    def is_valid_number(cur,i,incr):
        if incr:
            cur += 10 ** (l-i-1) - 1
            return cur > n
        else:
            return cur < n

    def digital_counter(delta_cost,incr):

        DP_SIZE = 300
        INF = int(1e20)
        dp = [[[(0,INF)]*DP_SIZE for _ in range(10)] for _ in range(l+1)] #(num,cost) [iter][last_num][delta]
        dp[0][0][0] = (0,0)

        for i in range(l):
            for num,delta,cost in delta_cost[l-i-1]:
                for j in range(10):
                    for k in range(-DP_SIZE//2, DP_SIZE//2):
                        if dp[i][j][k][1] != INF:

                            #fill dp

                            old_num, old_cost = dp[i][j][k]
                            new_num = old_num + num
                            new_cost = old_cost + cost
                            digit = num // (10**(l-i-1))
                            if is_valid_number(new_num,i,incr) and dp[i+1][digit][k+delta][1] > new_cost:
                                dp[i+1][digit][k+delta] = (new_num,new_cost)

    ##    for row in dp:
    ##        print(row)
    ##    print('')
        return min(dp[l][j][0][1] for j in range(10))

    return min(digital_counter(delta_cost_incr,True), digital_counter(delta_cost_decr,False), 10**l) * (10 ** (one_or_eight*2))

##n_str = input()
##print(solve(n_str))
counted = []
for i in range(100000):
    if i % 100 == 11 or i % 100 == 88:
        n = str(i).zfill(5)
        counted.append(solve(n))

import pickle

with open('dp_count_1188_fixed.pickle','wb') as fw:
    pickle.dump(counted,fw)