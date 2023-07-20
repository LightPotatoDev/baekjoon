import string

s = input()
alphabet = list(string.ascii_lowercase)
L = []

for i in alphabet:
    L.append(s.find(i))

print(' '.join(map(str,L)))

# index(), find() is almost same
# not found ->
# index(): exception
# fint() : return -1