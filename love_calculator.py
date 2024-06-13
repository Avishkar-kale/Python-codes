name = input("enter your name")
pname = input("enter your partner name")
combined_string = name + pname
string = combined_string.lower()
t = string.count('t')
r = string.count('r')
u = string.count('u')
e = string.count('e')
true = t + r + u + e
l = string.count('l')
o = string.count('o')
v = string.count('v')
e = string.count('e')
love = l + o + v + e

love_score = str(true)+str(love)
print(love_score)
love_score = int(str(true)+str(love))

if love_score<10 or love_score>90:
    print(f"your love score is {love_score} and you go like together cook and mentos")
elif(love_score>=40 and love_score<90):
    print(f"your love score is {love_score} and you alright together")
else:
    print(f"your love score is{love_score}.Thank you keep love you partner ")