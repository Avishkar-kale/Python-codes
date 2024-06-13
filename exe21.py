import math
def can_cal(height,width,cover):
    no_of_cans =height*width/cover
    no_of_cans = math.ceil(height*width/cover)
    print(f"you need {no_of_cans} no_of_cans")

h=int(input("enter height of wall in meters:"))
w=int(input("enter width of wall in meters:"))
coverage=7
can_cal(height=h,width=w,cover=coverage)
