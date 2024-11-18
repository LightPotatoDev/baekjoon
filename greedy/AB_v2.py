s = input()
t = input()

sB = s.count('B')
tB = t.count('B')
if (tB - sB) % 2 == 1:
    s = s[::-1]

def search(i):
    for j in range(len(s)):
        if s[j] != t[i+j]:
            return False
    return True

def makeAB(start):
    st = ['a']*len(t)
    putRight = (tB - sB) % 2 == 0
    for i in range(start,start+len(s)):
        st[i] = s[i-start]

    lIdx = start-1
    rIdx = start+len(s)
    while True:
        if putRight:
            if rIdx >= len(t) or t[rIdx] == 'B':
                putRight = False
                if lIdx < 0:
                    break
                st[lIdx] = 'B'
                lIdx -= 1
            else:
                st[rIdx] = 'A'
                rIdx += 1

        elif not putRight:
            if lIdx < 0 or t[lIdx] == 'B':
                putRight = True
                if rIdx >= len(t):
                    break
                st[rIdx] = 'B'
                rIdx += 1
            else:
                st[lIdx] = 'A'
                lIdx -= 1

    return ''.join(st)

for i in range(len(t)-len(s)+1):
    if search(i):
        if makeAB(i) == t:
            print(1)
            exit()

print(0)