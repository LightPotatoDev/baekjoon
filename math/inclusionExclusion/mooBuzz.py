n = int(input())
L = (1,2,4,7,8,11,13,14)
print(((n-1)//8)*15 + L[(n-1)%8])