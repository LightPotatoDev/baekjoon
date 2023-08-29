n,c = map(int,input().split())
L = list(input().split())
L.sort(reverse = True)
seq = []

def vowelCount(s):
    vowel, conson = 0,0
    for i in s:
        if i in ['a','e','i','o','u']:
            vowel += 1
        else:
            conson += 1
    return (vowel, conson)

def picknumber(L,index,subset):
    global seq
    if index >= n:
        vowel, conson = vowelCount(subset)
        if vowel >= 1 and conson >= 2:
            seq.append(subset)
        return

    A = L[:]
    for i in range(len(L)):
        p = A.pop()
        picknumber(A,index+1,subset+[p])

picknumber(L,0,[])
for i in seq:
    print(''.join(map(str,i)))