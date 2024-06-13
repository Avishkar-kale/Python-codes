size = input('what size of pizza you want(S/M/L)?')
bill = 0
if(size=='S' or size=='s'):
    bill=bill+100
    print("small pizza price is 100rs")
elif(size=='m' or size=='M'):
    bill = bill+200
    print("medium pizza price is 200rs")
else:
    bill += 300
extra_pepperoni = input("you want extra prpporani(S/N)?")
if(extra_pepperoni=='s' or extra_pepperoni=='S'):
    if(size=='s' or size=='S'):
        bill += 30
    else:
        bill += 50
extra_cheez = input("do you want to extra cheez?(Y/N)")
if(extra_cheez=='s' or extra_cheez=='S'):
    bill+=20

print(f"your total bill is{bill}")
