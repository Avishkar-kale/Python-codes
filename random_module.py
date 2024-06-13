import random
a=random.randint(1,6)#print any random number between 1 to 6 both numbers are included
print(a)
b=random.randrange(1,9)# in this function only a is included not b means 1 include but not 9
print(b)
c=random.uniform(1,5)#in this function we can set the limit for creating floating points
print(c)
list=[1,2,3,4,5,6,7,8,9,10,14]
d=random.choice(list)#this function choice any number from list provided by you
print(d)
random.shuffle(list)# this function shuffle the list provided by you
print(list)
e=random.random()#this function also print random number btw 0.01 to 9.99
print(e)

