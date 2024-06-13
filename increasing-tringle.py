print("This is the example of increasing tringle program")
num = int(input("enter a number"))
for i in range(num):
    # for j in range(num+i):
    #     print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print('\n')