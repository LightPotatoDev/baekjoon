L = [i for i in range(1,51)]
windows = [0] * 51

for m in L:
    windows = [0] * 51
    for i in range(1,m+1):
        for j in range(i,m+1,i):
            windows[j] = (windows[j]+1)%2

    print(windows,sum(windows))