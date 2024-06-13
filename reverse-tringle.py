print('This is the example of reverse tringle')
num = int(input("Enter a number of rows"))
for i in range(num):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(num-i):
        print("*", end=' ')
    for j in range(1,num-i):
        print("*", end=' ')
    print('\n')

