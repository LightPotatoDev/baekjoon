alpha = ('c=','c-','dz=','d-','lj','nj','s=','z=')
s = input()

for i in alpha:
    s = s.replace(i,'0')
print(len(s))