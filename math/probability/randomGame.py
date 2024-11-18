import sys
input = sys.stdin.readline

n = int(input())
while True:
    print("? 1")
    sys.stdout.flush()
    res = input().rstrip()
    if res == "Y":
        break
print("! 1")