s = input()
n = len(s)

def flip(end):
    global s
    sLeft = s[0:end+1]
    sRight = ""
    if end < n - 1:
        sRight = s[end+1:]
    s = sLeft[::-1] + sRight

curMax = s[0]
for i in range(n):
    if ord(curMax) > ord(s[i]):
        curMax = s[i]

    if i != n-1 and s[i] == curMax and ord(s[i+1]) > ord(s[i]):
        flip(i)
    elif i != n-1 and ord(s[i]) > ord(s[0]) >= ord(s[i+1]):
        flip(i)

if s[0] != curMax:
    flip(n-1)
print(s)