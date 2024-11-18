s,e = input().split()
sh,sm = map(int,s.split(":"))
start = sh*60+sm
eh,em = map(int,e.split(":"))
end = eh*60+em

n,t = map(int,input().split())
time = start
days = 0
for _ in range(n+1):
    if time+t < end:
        time += t
    else:
        time = start+t
        days += 1

print(days)
hh,mm = time // 60, time % 60
print(str(hh).zfill(2) + ":" + str(mm).zfill(2))