for i in range(2000):
    for j in range(2000):
        if (i+j)%2 == 0:
            print('.',end='')
        else:
            print('O',end='')
    print('')