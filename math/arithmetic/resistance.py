D = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4,
    "green":5, "blue":6, "violet":7, "grey":8, "white":9}

n = 0
n += 10*D[input()]
n += D[input()]
n *= 10 ** D[input()]
print(n)