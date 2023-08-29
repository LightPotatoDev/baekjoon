S = list(input()) + [' ']

words = []
word = []
isTag = False
for i in S:
    if isTag == False:
        if i == '<':
            isTag = True
            words.append(''.join(word[::-1]))
            word = []
            word.append(i)
        elif i == ' ':
            words.append(''.join(word[::-1]))
            words.append(' ')
            word = []
        else:
            word.append(i)
    else:
        word.append(i)
        if i == ">":
            isTag = False
            words.append(''.join(word))
            word = []

print(''.join(words))

"""
 temp = s[start:i]
 temp.reverse()
 s[start:i] = temp
"""