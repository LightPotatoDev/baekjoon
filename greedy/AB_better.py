S = input()
T = list(input())
len_s, len_t = len(S), len(T)
for _ in range(len_t - len_s):
    last = T.pop()
    if last == 'B':
        T = T[::-1]

print(1 if S == ''.join(T) else 0)

#https://www.acmicpc.net/source/73758482
#역으로 T에서 문자를 빼기