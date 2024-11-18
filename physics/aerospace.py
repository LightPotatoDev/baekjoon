import sys
input = sys.stdin.readline

k = int(input())
for tc in range(k):
    n,M = map(float,input().split())
    n = int(n)
    mass = []
    time = []
    force = []
    for _ in range(n):
        m,t,f = map(float,input().split())
        mass.append(m)
        time.append(t)
        force.append(f)

    spd = 0
    dist = 0
    for i in range(n):
        curMass = M + sum(mass[i:n])
        a = force[i] / curMass - 9.81
        dist += spd * time[i] + 1/2 * a * time[i]**2
        spd = spd + a * time[i]

    print(f"Data Set {tc+1}:")
    print("{:.2f}".format(round(dist,2)))
    print('')