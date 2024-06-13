number = [10, 0, -1, 7, 8, -6, 7]
print(number)
print(number[3])
number.reverse()
print(number)
number.sort()#for sorting list
print(number)

print(max(number))#find the max number in list
print(min(number))#find the min number in list
print(number[-1])
number.append(56)#add element at the last
print(number)
number.insert(2,45) #for adding element on specific position
print(number)
number.extend([25,45,36,56,89,89])# for add two or more number at a time
print(number)
number.remove(45)
print(number)
number[4]=45
print(number)
number[1:4]=[100,200,]
print(number)
