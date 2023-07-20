while True:
    L = list(map(int,input().split()))
    if L[0] == 0:
        break

    L.sort()
    if L[2] >= L[0] + L[1]:
        print("Invalid")
        continue

    S = set(L)
    tris = ("Equilateral","Isosceles","Scalene")
    print(tris[len(S)-1])