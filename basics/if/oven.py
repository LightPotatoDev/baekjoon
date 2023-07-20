h, m = map(int, input().split())
time = int(input())
plusHour = (m + time) // 60
print((h+plusHour) % 24, (m+time) % 60)