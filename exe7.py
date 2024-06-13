weight = input('enter your weight ij kg:')
height = input('enter your height in meter:')
bmi = int(weight) / float(height)**2
if bmi < 18.5:
    print("you are underweight")
elif bmi < 24.5:
    print("you are Normal weight")
elif bmi < 29.9:
    print("you are oveweight")
elif bmi < 34.9:
    print("you are Obesity class1")
elif bmi < 39.9:
    print("you are Obesity class2")
else:
    print("you are obesity class3")
print("Thank You")
