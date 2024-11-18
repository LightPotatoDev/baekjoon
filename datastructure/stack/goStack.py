import sys
input = sys.stdin.readline

def goStack(C,N):
    def errorCheck(cmd):
        if cmd in ["POP","INV","DUP"] and len(stk) < 1:
            return True
        elif cmd in ["SWP","ADD","SUB","MUL","DIV","MOD"] and len(stk) < 2:
            return True
        elif cmd in ["DIV","MOD"] and stk[-1] == 0:
            return True
        elif stk and abs(stk[-1]) > int(1e9):
            return True
        return False

    def arithmetic(cmd):
        a = stk.pop()
        b = stk.pop()
        if cmd == "ADD":
            stk.append(a+b)

        elif cmd == "SUB":
            stk.append(b-a)

        elif cmd == "MUL":
            stk.append(a*b)

        elif cmd == "DIV":
            c = abs(b) // abs(a)
            if a*b < 0:
                c *= -1
            stk.append(c)

        elif cmd == "MOD":
            c = abs(b) % abs(a)
            if b < 0:
                c *= -1
            stk.append(c)

    for n in N:
        stk = [n]
        err = False
        for cmd in C:
            if errorCheck(cmd):
                err = True
                break

            if cmd[:3] == "NUM":
                x = int(cmd.split()[1])
                stk.append(x)

            elif cmd == "POP":
                stk.pop()

            elif cmd == "INV":
                stk[-1] *= -1

            elif cmd == "DUP":
                stk.append(stk[-1])

            elif cmd == "SWP":
                stk[-1],stk[-2] = stk[-2],stk[-1]

            else:
                arithmetic(cmd)

        if err or len(stk) != 1 or abs(stk[-1]) > int(1e9):
            print("ERROR")
        else:
            print(stk[0])

cmd = []
while True:
    c = input().rstrip()
    if c == "QUIT":
        break
    elif c == "END":
        n = int(input())
        N = [int(input()) for _ in range(n)]
        goStack(cmd,N)
        cmd = []
        print('')
    elif c != '':
        cmd.append(c)