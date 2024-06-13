height = int(input("enter your heiht in feet"))
if(height>3):
    print("you can ride")
    age = int(input("enter your current age"))
    if(age<12):
        print("pay only 150rs")
    elif(age<=18):
        print("pay only 250rs")
    else:
        print("pay only 500rs ")
else:
    print("soory you cannot ride")
print("Thank you for visiting see you soon next time BBy!")