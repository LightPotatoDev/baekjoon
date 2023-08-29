n = int(input())
L = ["SK","CY"]
rule = [0,1,0,0,0,0,1]
print(L[rule[(n-1)%7]])