print("this is the example diamond pattern program")
num = int(input('Enter a number of rows'))
for i in range(num):
    for j in range(num-i):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print('\n')
for k in range(num):
    for j in range(k+1):
        print(' ',end=' ')
    for j in range(num-k):
        print('*',end=' ')
    for j in range(1,num - k):
        print('*', end=' ')

    print('\n')
