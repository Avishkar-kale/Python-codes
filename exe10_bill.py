names = input("enter your any 4 friends name")
s_name = names.split(",")
import random
str_l = len(s_name)
print(str_l)
r_numbers=random.randint(0,str_l-1)
print(s_name)
print(f"{s_name[r_numbers]} pay the bill")

