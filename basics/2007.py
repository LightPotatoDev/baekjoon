x,y = map(int,input().split())
week = ("SUN","MON","TUE","WED","THU","FRI","SAT")
days = (31,28,31,30,31,30,31,31,30,31,30,31)

dayCnt = sum(days[:x-1])+y
print(week[dayCnt%7])