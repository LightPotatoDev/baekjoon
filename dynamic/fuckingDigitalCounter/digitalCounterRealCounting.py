lines = [6,2,5,5,4,5,6,3,7,5]

def count_lines(n):
    res = 0
    for s in n:
        res += lines[int(s)]
    return res

f = open('digital_counter_0_to_999','w')

for i in range(1000):
    n = str(i).zfill(3)
    f.write(str(n) + ' ' +  str(count_lines(n)))
    f.write('\n')

f.close()