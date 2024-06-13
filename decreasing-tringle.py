print("this is the example of decreasing tringle")

num = int(input("Enter a number of rows"))
for i in range(num):
    for j in range(num-i):
        print('*',end=" ")
    print('\n')