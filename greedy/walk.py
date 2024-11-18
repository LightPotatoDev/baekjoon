x,y,w,s = map(int,input().split())
diag = 0
if w*2 > s:
    diag = min(x,y)
    x -= diag
    y -= diag
if w > s:
    extraDiag = max(x,y)//2
    diag += extraDiag*2
    if x > 0:
        x -= extraDiag*2
    if y > 0:
        y -= extraDiag*2

print(diag*s+(x+y)*w)