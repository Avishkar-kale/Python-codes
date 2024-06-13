# f1 = open("file_1.txt", "r+")
# f1.write("hii this is the example of file handler")
# print(f1.seek(0))
# print(f1.read())

f2 = open("file_2.txt", "a+")
f2.write("this is the example of append in file handler")
print(f2.seek(0))
print(f2.read())
