n = int(input())
s = input()

def failure(s):
    l = len(s)
    lps = [0] * l
    i,match = 1,0

    while i < l:
        if s[i] == s[match]:
            match += 1
            lps[i] = match
            i += 1
        else:
            if match == 0:
                i += 1
            else:
                match = lps[match-1]

    return lps

print(failure(s))