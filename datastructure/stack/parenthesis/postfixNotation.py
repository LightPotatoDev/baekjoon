s = input()
oper = {"*","/","+","-"}
maxdepth = 5
operInd = [[] for _ in range(maxdepth)]
order = []
stk = []

op = 0
def setOperation(o1,o2):
    global op
    for x in s:
        l = len(stk)
        if x == o1 or x == o2:
            operInd[l].append(op)
            op += 1
        elif x == "(":
            stk.append(s[op])
        elif x == ")":
            stk.pop()

setOperation("*","/")
setOperation("+","-")
for i in range(maxdepth-1,-1,-1):
    order.extend(operInd[i])
print(operInd)
print(order)