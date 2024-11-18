import math

a = int(input())/100
b = int(input())/100

AProb = 0
BProb = 0
Prime = [2,3,5,7,11,13,17]

for i in Prime:
    AProb += math.comb(18,i)*(a**i)*((1-a)**(18-i))
    BProb += math.comb(18,i)*(b**i)*((1-b)**(18-i))

print(AProb + BProb - AProb*BProb)