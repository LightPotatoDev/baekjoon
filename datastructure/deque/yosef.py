from collections import deque
n,k = map(int,input().split())
L = deque([i+1 for i in range(n)])

result = []
for _ in range(n):
    L.rotate((k-1)*-1)
    result.append(L.popleft())
print(f"<{', '.join(map(str,result))}>")