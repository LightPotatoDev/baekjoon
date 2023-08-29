import sys
input = sys.stdin.readline
import math

n = int(input())

def KMP(p):
    l = len(p)
    table = [0] * (l+1)
    start,match = 1,0
    while start+match < l:
        if p[start+match] == p[match]:
            match += 1
            table[start+match] = match
        else:
            if match == 0:
                start += 1
            else:
                start += match - table[match]
                match = table[match]

    return table[-1]

s = ''.join(input().split())
input()

repeat = n - KMP(s)
if len(s) % repeat == 0:
    repTimes = n // repeat
    gcd = math.gcd(repTimes,n)
    print(f"{repTimes // gcd}/{n // gcd}")
else:
    print(f"1/{n}")