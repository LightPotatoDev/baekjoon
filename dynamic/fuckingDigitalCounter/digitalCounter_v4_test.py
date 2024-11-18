lines = [6,2,5,5,4,5,6,3,7,5]
diff = [[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        diff[i][j] = lines[j]-lines[i]
DP_SIZE = 300
INF = int(1e20)

def solve(n_str):
    def is_valid_number(n_str,cur,i,incr):
        n = int(n_str)
        l = len(n_str)
        if incr:
            cur += 10 ** (l-i-1) - 1
            return cur > n
        else:
            return cur < n

    def digital_counter(n_str,delta_cost,incr):
        l = len(n_str)
        dp = [[[(0,INF)]*DP_SIZE for _ in range(10)] for _ in range(l+1)] #(num,cost) [iter][last_num][delta]
        dp[0][0][0] = (0,0)

        for i in range(l):
            for num,delta,cost in delta_cost[l-i-1]:
                for j in range(10):
                    for k in range(-DP_SIZE//2, DP_SIZE//2):
                        if dp[i][j][k][1] != INF:

                            old_num, old_cost = dp[i][j][k]
                            new_num = old_num + num
                            new_cost = old_cost + cost
                            digit = num // (10**(l-i-1))
                            if is_valid_number(n_str,new_num,i,incr) and dp[i+1][digit][k+delta][1] > new_cost:
                                dp[i+1][digit][k+delta] = (new_num,new_cost)

    ##    for row in dp:
    ##        print(row)
    ##    print('')
        return min(dp[l][j][0][1] for j in range(10))

    def find_delta_cost(n_str):
        n = int(n_str)
        l = len(n_str)

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

        return (delta_cost_incr, delta_cost_decr)

    def normal(n_str):
        delta_cost_incr, delta_cost_decr = find_delta_cost(n_str)
        return min(digital_counter(n_str,delta_cost_incr,True), digital_counter(n_str,delta_cost_decr,False))

    def one_or_eight(n_str):
        ooe = 0
        n = int(n_str)

        while (n % 100 == 11 or n % 100 == 88) and len(n_str) >= 3:
            ooe += 1
            n //= 100
            n_str = n_str[:-2]

        delta_cost_incr, delta_cost_decr = find_delta_cost(n_str)
        return min(digital_counter(n_str,delta_cost_incr,True), digital_counter(n_str,delta_cost_decr,False)) * (10 ** ooe*2)

    return min(normal(n_str), one_or_eight(n_str), 10**len(n_str))

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