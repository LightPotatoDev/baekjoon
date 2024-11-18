s = input()
oper = {"*","/","+","-"}
maxdepth = 50
operInd = [[] for _ in range(maxdepth)]
orderInd = []

stk = []
def setOperation(o1,o2):
    for i,x in enumerate(s):
        l = len(stk)
        if x == o1 or x == o2:
            operInd[l].append(i)
        elif s[i] == "(":
            stk.append(s[i])
        elif s[i] == ")":
            stk.pop()

setOperation("*","/")
setOperation("+","-")
for i in range(maxdepth-1,-1,-1):
    orderInd.extend(operInd[i])

order = [0]*len(orderInd)
ind = 0
for i in range(100):
    if i in orderInd:
        order[orderInd.index(i)] = ind
        ind += 1

def findOperand(ind,dir):
    ind += dir
    while s[ind] == "":
        ind += dir
    return ind

s = list(filter(lambda x:x!="(" and x != ")", s))
for i in order:
    op = s[2*i+1]
    opand1 = findOperand(2*i+1,-1)
    opand2 = findOperand(2*i+1, 1)
    s[2*i+1] = s[opand1]+s[opand2]+op
    s[opand1] = ''
    s[opand2] = ''

print(''.join(s))