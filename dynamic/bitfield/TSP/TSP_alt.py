import sys
input = sys.stdin.readline
INF = sys.maxsize


def find_path(last, visited):
    if visited == visited_all:
        return W[last][0] or INF
    if cache[last][visited]:
        return cache[last][visited]
    tmp = INF
    for city in range(N):
        if not (visited & (1 << city)) and W[last][city]:
            tmp = min(tmp, find_path(city, visited | (1 << city)) + W[last][city])
    cache[last][visited] = tmp
    return tmp


N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
cache = [[0] * (1 << N) for _ in range(N)]
visited_all = (1 << N) - 1
print(find_path(0, 1 << 0))

#dannyp0930