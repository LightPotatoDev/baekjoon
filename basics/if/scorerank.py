score = int(input())
cuts = (90, 80, 70, 60, 0)
ranks = ('A', 'B', 'C', 'D', 'F')

for i in range(5):
    if score >= cuts[i]:
        print(ranks[i])
        break