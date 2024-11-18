import sys
input = sys.stdin.readline

whole_doc = []
while True:
    inp = input().strip()
    if inp == '<?end?>':
        break
    else:
        whole_doc.append(inp)

part_doc = []
part_docs = []
n = len(whole_doc)
for i in range(1,n+1):
    if i == n or whole_doc[i] == '<?xml version="1.0"?>':
        part_docs.append(part_doc)
        part_doc = []
    else:
        part_doc.append(whole_doc[i])

def parse_doc(doc):
    elements = []
    ele = []
    is_element = False
    attributes = []

    for i in range(len(doc)):
        for j in range(len(doc[i])):
            t = doc[i][j]
            if is_element == False and t == '<':
                is_element = True
            elif is_element == True:
                if t == '>':
                    is_element = False
                    ele_attr = ''.join(ele).split()
                    elements.append(ele_attr[0])
                    if len(ele_attr) > 1:
                        attributes.append(ele_attr[1:])
                    ele = []
                else:
                    ele.append(t)
    return (elements, attributes)

def check_closure(elem):
    if len(elem) == 0:
        return False

    stk = []
    for i,e in enumerate(elem):
        if e[-1] == '/':
            continue
        if e[0] != '/':
            if e in stk:
                return False
            stk.append(e)
        if e[0] == '/':
            if len(stk) == 0:
                return False
            if stk[-1] != e[1:]:
                return False
            stk.pop()
        if len(stk) == 0 and i != len(elem) - 1:
            return False

    return len(stk) == 0

def check_attributes(attr):
    for a in attr:
        a_dict = set()
        for prop in a:
            if '=' not in prop:
                return False
            k,v = prop.split('=')
            if k in a_dict:
                return False
            a_dict.add(k)

    return True

def check_well_formedness(doc):
    elements, attributes = parse_doc(doc)
    res = check_closure(elements)
    res2 = check_attributes(attributes)

    return res and res2

for doc in part_docs:
    if check_well_formedness(doc) == True:
        print('well-formed')
    else:
        print('non well-formed')