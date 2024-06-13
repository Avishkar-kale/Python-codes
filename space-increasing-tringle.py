print("this is the examale of space incrasing tringle")
num = int(input('Enter a number of rows'))
for i in range(num):
    # for j in range(i+1):
    #     print(' ',end=' ')
    for j in range(num-i):
            print('*', end=' ')
    print('\n')