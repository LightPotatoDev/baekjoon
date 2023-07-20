x, y, w, h = map(int,input().split())
L = [w-x, h-y, x, y]
print(min(L))