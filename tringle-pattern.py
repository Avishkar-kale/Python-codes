print("This is the example of tringle")
num = int(input("Enter a number"))
for i in range(num):
    for j in range(num-i):
        print(' ',end=' ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print('\n')