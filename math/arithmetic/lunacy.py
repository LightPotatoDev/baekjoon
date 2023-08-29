while True:
    n = float(input())
    if n < 0:
        break
    moon = "{:.2f}".format(n*0.167)
    n = "{:.2f}".format(n)
    print(f"Objects weighing {n} on Earth will weigh {moon} on the moon.")