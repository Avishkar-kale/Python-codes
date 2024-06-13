height = int(input("enter your height"))
if(height>3):
    print("you can ride")
    age = int(input("enter your age"))
    if(age<12):
        bill = 150
        print("your ticket bill is 150rs")
    elif(age<18):
        bill = 250
        print("your ticket bill is 250rs")
    elif(age>=18):
        bill = 500
        print("you ticket bill is 500rs")
    photos = input("you want to photos during ride(Y/N)")
    if(photos=='Y' or photos=='y'):
        bill = bill+50
        print(f"your current bill is {bill}")
    else:
        print(f"pay only {bill}")
        print("Thank you for visiting our ride club!")
else:
    print("sorry you cannot ride")
    print("Thank you for visiting our ride club!")