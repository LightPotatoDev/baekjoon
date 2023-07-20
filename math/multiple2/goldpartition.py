T = int(input())

def sieve(n):
    p = 2
    prime = [1 for i in range(n+1)]
    for i in range(2,int(n**0.5)+1):
        if prime[i] == 0:
            continue
        for j in range(2,n//i+1):
            prime[j*i] = 0
    prime[0:2] = [0,0]
    return prime

isprime = sieve(1000000)

for _ in range(T):
    n = int(input())
    if n == 4:
        print(1)
        continue

    l_pointer = n//2 - int(n%4==0)
    r_pointer = n//2 + int(n%4==0)
    partitions = 0

    while l_pointer > 2:
        if isprime[l_pointer] == 1 and isprime[r_pointer] == 1:
            partitions += 1
        l_pointer -= 2
        r_pointer += 2

    print(partitions)

#모든 테스트 케이스에서 공통으로 쓰이는 자료는 반복문 밖으로 뺄 수 있음