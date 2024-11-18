y,m,d = map(int,input().split("-"))
n = int(input())

d += n
m += (d-1)//30
d = (d-1)%30 + 1

y += (m-1)//12
m = (m-1)%12 + 1

print(f"{str(y).zfill(4)}-{str(m).zfill(2)}-{str(d).zfill(2)}")