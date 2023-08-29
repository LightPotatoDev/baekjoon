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

    for i,x in enumerate(table):
        if i <= 1:
            continue
        repeat = i - x
        if repeat != i and i % repeat == 0:
            print(i,i // repeat)


KMP(input())