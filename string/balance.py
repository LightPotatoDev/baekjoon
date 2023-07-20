import re

def vps(s):
    while True:
        s2 = s.replace("()","")
        s2 = s2.replace("[]","")
        if s2 == s:
            break
        s = s2

    if s == "":
        return "yes"
    else:
        return "no"

while True:
    s = input()
    if s == ".":
        break
    s = ''.join(re.findall("\(|\)|\[|\]", s))
    print(vps(s))