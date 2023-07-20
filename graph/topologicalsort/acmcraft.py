import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

T = int(input())

def getReqbuilds(trees, final):

    reqbuilds = []
    def getTree(trees, next, req):

        connected = []
        for i in trees:
            if i[1] == next:
                connected.append(i[0])

        if len(connected) == 0:
            reqbuilds.append(req + [final])
            return

        for i in connected:
            getTree(trees, i, req+[i])

    getTree(trees, final, [])
    return reqbuilds


def timecalc(reqbuilds, times):

    timesums = []

    for i in reqbuilds: #i = [2,1,4]
        timesum = 0
        for j in i:
            timesum += times[j-1]
        timesums.append(timesum)

    return max(timesums)

for _ in range(T):
    build, rules = map(int,input().split())
    times = list(map(int, input().split()))
    trees = [list(map(int, input().split())) for _ in range(rules)]
    final = int(input())

    requiredBuilds = getReqbuilds(trees, final)
    print(timecalc(requiredBuilds, times))