s = input()
f = input()
vowels = {'a','e','i','o','u','y'}
s = s.lower()
f = f.lower()

i = 0
j = 0
res = 'Different'
while i < len(s) and j < len(f):
    if s[i] == f[j]:
        i += 1
        j += 1
    elif f[j] in vowels:
        j += 1
    else:
        break

if i == len(s):
    res = 'Same'
    for letter in f[j:]:
        if letter not in vowels:
            res = 'Different'
            break

print(res)