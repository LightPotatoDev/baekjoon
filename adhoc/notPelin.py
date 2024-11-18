s = input()

if len(set(s)) == 1:
    print(-1)
    exit(0)

if s == s[::-1]:
    print(len(s)-1)
else:
    print(len(s))