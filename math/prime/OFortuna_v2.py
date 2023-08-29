N = list(map(int,input().split()))
fortuneL = [5,7,13,23,17,19,23,37,61,67,61,71,47]
lessL = [3,7,11,13,17,29,23,43,41,73,59,47,89]

for n in N:
    print(f"N = {n} FORTUNATE = {fortuneL[n-2]} LESS = {lessL[n-2]}")

