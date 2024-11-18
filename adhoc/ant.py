w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())

A = [i for i in range(w)] + [w-i for i in range(w)]
B = [i for i in range(h)] + [h-i for i in range(h)]
print(A[(p+t)%(w*2)], B[(q+t)%(h*2)])