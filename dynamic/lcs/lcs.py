s1 = input()
s2 = input()

def getlcs(s1,s2):
    lcs = 0
    index = 0
    for i in range(len(s2)):
        for j in range(index,min(i+1,len(s1))):
            if s1[j] == s2[i]:
                index = j+1
                lcs += 1
                break
    return lcs

print(getlcs(s1,s2), getlcs(s2,s1))