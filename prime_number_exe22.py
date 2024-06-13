
num=int(input("enter number"))
def prime_number(number):
    count=0
    for i in range(2,number+1):
        if number%number==0:
            if number%i==0:
                count+=1
    if count==1:
        print("enterd no is prime number")
    else:
        print("entered no is not prime number")



prime_number(num) 
