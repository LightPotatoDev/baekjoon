n = int(input())
m = int(input())
s = input()

p = "I" + "OI" * n

cnt = 0
i = 0 #pointer
combo = False

while True:
    if combo == False:
        if i > m-2*n:
            break
        elif p == s[i:i+2*n+1]:
            cnt += 1
            combo = True
            i += 2*n + 1
        else:
            i += 1
    else:
        if i > m-2:
            break
        elif s[i:i+2] == "OI":
            cnt += 1
            i += 2
        else:
            combo = False

print(cnt)

""" by omj0722
while (i < (M-1)):
  if S[i:i+3] == 'IOI':
    i += 2
    check += 1
    if check == N:
      cnt += 1
      check -= 1

  else:
    i += 1
    check = 0

    IOIOIOI... 전체를 비교하지 않고 IOI 파트까지만 비교해서 연산 횟수를 줄이기
"""