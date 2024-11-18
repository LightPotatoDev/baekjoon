n,p = map(int,input().split())
B = list(map(int,input().split()))
mod_list = [0]*p
for i in range(1,n+1):
    mod_list[i%p] += 1

if p == 1:
    if B == [i for i in range(1,n+1)]:
        print("YES")
    else:
        print("NO")
    exit()

max_mod = max(mod_list)
num = [0]*max_mod
num[max_mod-1] = mod_list.count(max_mod)
for i in range(max_mod-1):
    num[i] = p
print(num)