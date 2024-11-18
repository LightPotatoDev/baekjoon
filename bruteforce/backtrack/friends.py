import sys
input = sys.stdin.readline

f,r = map(int,input().split())
n = int(input())
c = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
total = 0
for _ in range(c):
    a,b,m = map(int,input().split())
    graph[a][b] += m
    graph[b][a] += m
    total += m
ans = 0
ans_choice = [0]*(n+1)

def friends(u,choice,chosen_num,minute):
    global ans, ans_choice
    if u > n:
        if minute > ans:
            ans = minute
            ans_choice = choice.copy()
        return

    if choice[u] == 0:
        for v in range(u, n+1):
            if graph[u][v] > 0 and choice[v] == 0:
                choice[u] = chosen_num+1
                choice[v] = chosen_num+1
                friends(u+1,choice,chosen_num+1,minute+graph[u][v])
                choice[u] = 0
                choice[v] = 0
    friends(u+1,choice,chosen_num,minute)

friends(1,[0]*(n+1),0,0)

print((total-ans)*r + ans*f)
for i in range(1,n//2+1):
    a,b = 0,0
    for j in range(1,n+1):
        if ans_choice[j] == i:
            if a == 0:
                a = j
            else:
                b = j
    if a != 0 and b != 0:
        print(a,b)