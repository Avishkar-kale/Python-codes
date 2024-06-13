
count = 0
def count_string(input_string):
    # global count
    count = 0
    for char in input_string:
        count += 1
    return count
input_string=input('Enter string:')
lenght = count_string(input_string)
print(f'lenght of string is:={lenght}')

