from math import comb,factorial

def onto(m,n):
    s = 0
    for i in range(n+1):
        s += (-1)**i * comb(n,n-i) * (n-i)**m
    return s

#|A| = m, |B| = n
# A->B로 대응되는 onto 함수의 개수 (B의 모든 원소가 적어도 1번 선택됨)
# m >= n

def stirling(m,n):
    s = 0
    for i in range(n+1):
        s += (-1)**i * comb(n,n-i) * (n-i)**m
    return s // factorial(n)

print(stirling(4,7))