import re

s = input()
bomb = input()

L = re.finditer(bomb,s)
starts = []
for i in L:
    spans.append(i.start())

print(starts)

while starts:
