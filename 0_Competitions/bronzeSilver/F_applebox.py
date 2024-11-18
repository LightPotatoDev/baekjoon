n = int(input())
mass = 0
gold = 0

for _ in range(n):
    inp = input().split()
    t = inp[0]
    w,h,l = map(int,inp[1:])

    if t == "A":
        apples = (w//12) * (h//12) * (l//12)
        mass += apples * 500 + 1000
        gold += apples * 4000
    elif t == "B":
        mass += 6000

print(mass)
print(gold)