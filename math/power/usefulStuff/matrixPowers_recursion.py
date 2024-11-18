K = 1000


def mul(a, b, n):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    for i in range(n):
        for j in range(n):
            result[i][j] %= K
    return result


def exp(f, n):
    if n == 1 or n == 0:
        return f
    temp = exp(f, n // 2)
    if n % 2 == 1:
        return mul(mul(temp, temp, x), f, x)
    else:
        return mul(temp, temp, x)


while 1:
    x, y, z = map(int, input().split())
    if x == y == z == 0:
        break
    K = y
    mat = []
    for _ in range(x):
        s = input().split()
        mat.append([int(i) for i in s])

    mat = exp(mat, z)
    for i in range(x):
        mat[i] = [j % K for j in mat[i]]
    for i in range(x):
        mat[i] = [str(j) for j in mat[i]]
        print(' '.join(mat[i]))
    print()
