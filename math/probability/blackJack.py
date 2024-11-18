Meanings = {'A':11, 'K':10, 'Q':10, 'J':10, 'T':10}

while True:
    n = int(input())
    if n == 0:
        break
    L = [4*n]*12
    L[0],L[1],L[10] = 0,0,16*n
    Cards = list(input().split())
    deal, you = 0,0
    ans = 0

    for i,x in enumerate(Cards):
        if x in Meanings:
            x = Meanings[x]
        else:
            x = int(x)
        if i == 0:
            deal = x
        else:
            you += x
        L[x] -= 1
    if you >= 22:
        you -= 10

    for i in range(2,11):
        if deal+i < you:
            ans += 1/(52*n-3)*L[i]
    if deal == 11 and 12 < you:
        ans += 1/(52*n-3)*L[11]
    elif deal+11 < you:
        ans += 1/(52*n-3)*L[11]

    print('{:.3f}'.format(round(ans*100,3))+"%")
