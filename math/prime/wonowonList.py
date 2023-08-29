L = []
while True:
    try:
        L.append(int(input()))
    except:
        break

f = open("wonoL","w")
f.write(str(L))
f.close()