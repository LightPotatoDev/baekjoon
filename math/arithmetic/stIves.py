while True:
    n = float(input())
    if n == 0:
        break

    s = 0
    for i in range(5):
        s += n**i
    print("{:.2f}".format(round(s,2)))
