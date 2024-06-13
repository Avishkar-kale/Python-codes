year = int(input("which year you want to check"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("you entered year is not leap year")
    else:
        print("leap year")
else:
    print("Not leap year")