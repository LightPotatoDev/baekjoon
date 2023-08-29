s = input()
target = ("U","C","P","C")
p = 0

for i in s:
    if i == target[p]:
        p += 1
    if p == 4:
        print("I love UCPC")
        exit(0)

print("I hate UCPC")