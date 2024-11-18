import sys
input = sys.stdin.readline

def str_to_int(st):
    L = []
    for s in st:
        L.append(ord(s) - 97)
    return L

def int_to_str(L):
    st = []
    for i in L:
        st.append(chr(i+97))
    return ''.join(st)

def find_middle_word(n,s,t,k):
    s_list = str_to_int(s)
    t_list = str_to_int(t)

    res = "NO"

    while True:
        s_list[-1] += 1
        for i in range(n-1,0,-1):
            if s_list[i] >= 26:
                s_list[i] = 0
                s_list[i-1] += 1
        if s_list[0] >= 26:
            return "NO"
        if all([s_list[i] == t_list[i] for i in range(n-1,-1,-1)]):
            return "NO"
        for i in range(n-1,-1,-1):
            if s_list[i] == ord(k) - 97:
                return int_to_str(s_list)



T = int(input())
for _ in range(T):
    n,k = input().rstrip().split()
    n = int(n)
    s = input().rstrip()
    t = input().rstrip()

    ans = find_middle_word(n,s,t,k)
    print(ans)