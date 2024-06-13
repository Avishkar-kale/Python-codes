height = int(input("what is you height"))
if(height>3):
    print("you can ride")

    age = int(input("enter your age"))
    if(age<12):
        photos = int(input("if you want to capture photo during ride? if yes please press 1 or not press 2"))
        if(photos==1):
            print(("pay only 200rs"))
        else:
            print("pay only 150rs")
    elif(age<18):
        photos = int(input("if you want to capture photo during ride? if yes please press 1 or not press 2"))
        if (photos == 1):
            print(("pay only 300rs"))
        else:
            print("pay only 250rs")
    elif(age>=18):
        photos = int(input("if you want to capture photo during ride? if yes please press 1 or not press 2"))
        if (photos == 1):
            print(("pay only 550rs"))
        else:
            print("pay only 500rs")

else:
    print("sorry you can not ride")