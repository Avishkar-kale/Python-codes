number_list = input("enter number for list")
split_number = number_list.split()
print(split_number)
count =0
for i in split_number:
    count = count++1
print(f"the lenght of list is {count}")
for i in range(count):
    split_number[i] = int(split_number[i])
maximum_number = split_number[0]
for number in split_number:
    if number > maximum_number:
        maximum_number = number
print(f"the maximum number in list is :{maximum_number}")





