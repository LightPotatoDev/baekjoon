T = int(input())
for i in range(1,T+1):
    L = list(map(int,input().split()))
    L.sort()
    a,b,c = L

    type = ""

    if a+b <= c:
        type = "invalid!"
    elif a == b and b == c:
        type = "equilateral"
    elif a == b or b == c:
        type = "isosceles"
    else:
        type = "scalene"

    print(f"Case #{i}: {type}")

