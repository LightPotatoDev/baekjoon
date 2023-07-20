import math

n = int(input())
numbers = list(map(int,input().split()))
operators = list(map(int,input().split())) #+,-,*,//

mini = 10**9
maxi = -10**9

def insert(cur,index):

    global mini
    global maxi

    if index == n-1:
        if cur < mini:
            mini = cur
        if cur > maxi:
            maxi = cur
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            if i == 0:
                insert(cur+numbers[index+1],index+1)
            elif i == 1:
                insert(cur-numbers[index+1],index+1)
            elif i == 2:
                insert(cur*numbers[index+1],index+1)
            elif i == 3:
                if cur >= 0:
                    insert(cur//numbers[index+1],index+1)
                else:
                    insert(math.ceil(cur/numbers[index+1]),index+1)
            operators[i] += 1

insert(numbers[0],0)

print(maxi)
print(mini)

""" by hmlim01
def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
"""