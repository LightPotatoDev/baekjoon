from collections import deque

T = int(input())

def set_printing(papers):
    mostimp = [k for k,v in papers.items() if v == max(papers.values())]
    return mostimp

for _ in range(T):
    n, m = map(int,input().split())
    papers = dict()
    imp = list(map(int,input().split()))
    for i in range(n):
        papers[i]=imp[i]

    most = []
    order = 0

    while len(papers) > 0:
        if len(most) == 0:
            most = set_printing(papers)

        leftPaper = list(papers)[0]
        if leftPaper in most:
            order += 1
            if leftPaper == m:
                print(order)
                break
            del papers[leftPaper]
            most.remove(leftPaper)
        else:
            val = papers[leftPaper]
            papers.pop(leftPaper)
            papers[leftPaper] = val
