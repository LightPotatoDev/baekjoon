def KMP(p):
    l = len(p)
    table = [0] * (l+1)
    start,match = 1,0
    while start+match < l:
        if p[start+match] == p[match]:
            match += 1
            table[start+match] = match
        else:
            if match == 0:
                start += 1
            else:
                start += match - table[match]
                match = table[match]

    return table[-1]

while True:
    s = input()
    if s == ".":
        break

    repeat = len(s) - KMP(s)
    if len(s) % repeat == 0:
        print(len(s) // repeat)
    else:
        print(1)



