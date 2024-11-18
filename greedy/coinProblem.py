T = int(input())
values = [10**i for i in range(1,17)] + [25*(100**i) for i in range(0,8)]
values.sort()

for _ in range(T):
    n = int(input())
    ans = 0

    while n > 0:
        digits = len(str(n))
        two = n
        if digits >= 2:
            two = n // (10 ** (digits-2))

        if digits % 2 == 0 and ((30 <= two <= 34) or (40 <= two <= 44)):
            ans += (two//10)
            n -= (two//10) * (10 ** (digits-1))
        else:
            val = 1
            for v in values:
                if v <= n:
                    val = v
                else:
                    break
            ans += 1
            n -= val

    print(ans)

