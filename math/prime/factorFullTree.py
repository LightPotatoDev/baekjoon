import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.depth = 0
        self.idx = 0
        self.val = 0
        self.parent = 0

    def __repr__(self):
        return f'{self.depth} {self.idx+1} {self.val} {self.parent+1}'

def sieve(n):
    is_prime = [1] * (n//2+1)
    primes = [2]

    for i in range(1,n//2+1):
        if is_prime[i]:
            p = 2*i+1
            primes.append(p)
            for j in range((p**2)//2,n//2+1,p):
                is_prime[j] = 0

    return primes

primes = sieve(500)

n = int(input())
graph = [[] for _ in range(n)]
nodes = [Node() for _ in range(n)]
visited = [0]*n

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def dfs(u, depth, par):
    visited[u] = 1
    for v in graph[u]:
        if visited[v] == 0:
            dfs(v, depth+1, u)
    nodes[u].depth = depth
    nodes[u].idx = u
    nodes[u].parent = par

def find_depth(node):
    depth = 0
    while node.val == 0:
        node = nodes[node.parent]
        depth += 1
    return (depth, node.val)

def give_number(node):
    global cur_p_idx
    to_assign = []
    while node.val == 0:
        to_assign.append(node)
        node = nodes[node.parent]

    mul = node.val
    for i in range(len(to_assign)):
        to_assign[i].val = mul * primes[cur_p_idx] ** (len(to_assign)-i)
    cur_p_idx += 1

dfs(0,1,-1)
nodes[0].val = 1
cur_p_idx = 0

while True:
    max_depth = 0
    max_node = 0
    max_val = 0
    for node in nodes:
        d,v = find_depth(node)
        if d > max_depth:
            max_node = node
            max_depth = d
        elif d == max_depth and v > max_val:
            max_node = node
            max_val = v

    if max_depth == 0:
        break

    give_number(max_node)

for nd in nodes:
    print(nd.val, end=' ')