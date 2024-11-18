n,m = map(int,input().split())
people = list(map(int,input().split()))
places = list(map(int,input().split()))

people.sort(reverse = True)
places.sort(reverse = True)

ptr = 0
ans = 'YES'
for i in range(n):
    if ptr >= m:
        break
    place_left = m-ptr
    if people[i] < place_left:
        ans = 'NO'
        break

    places[ptr] -= 1
    if places[ptr] == 0:
        ptr += 1

print(ans)