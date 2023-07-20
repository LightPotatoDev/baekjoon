n = int(input())
score = []
score += [int(input()) for _ in range(n)]

def upstairs(x):
    steps = [[] for _ in range(x+1)]
    for i in range(1, x+1):
        if i == 1:
            steps[1].append([0,score[1]])
        elif i == 2:
            steps[2].append([0,score[2]])
            steps[2].append([1,score[1]+score[2]])
        else:
            max1 = max(j[1] for j in steps[i-2])
            steps[i].append([0,max1+score[i]])

            max2 = max(j[1] for j in steps[i-1] if j[0] != 1)
            steps[i].append([1,max2+score[i]])

    return steps[x]


print(max(j[1] for j in upstairs(n)))

""" by rnjsdn12332
s= int(input())
score = [0]

for i in range(0, s) :
    score.append(int(input()))

if s in [1,2] :
    print(sum(score))

else :

    dp = [0]*(s+1)

    dp[1] = score[1]
    dp[2] = score[1]+score[2]
    dp[3] = max(score[1], score[2])+score[3]


    for i in range(4, s+1) :
        dp[i] = max(dp[i-3]+score[i-1], dp[i-2])+score[i]

    print(dp[s])
"""