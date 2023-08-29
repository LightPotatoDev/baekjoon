import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[999]*(n+1) for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    graph[s][e] = 1

for i in range(1,n+1):
    graph[i][i] = 0

def floyd():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

floyd()

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == 999:
            graph[i][j] = 0

cnt = 0
for i in range(1,n+1):
    cnt += 1
    for j in range(1,n+1):
        if graph[i][j] > 0 or graph[j][i] > 0 or i == j:
            pass
        else:
            cnt -= 1
            break

print(cnt)


"""
frmt = "{:>5}"*(n)
for row in graph[1:]:
    print(frmt.format(*row[1:]))
print('')
"""