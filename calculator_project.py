import os

def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

operations_dict={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}
def calculator():
    number1 = float(input("Enter first number:-"))
    for i in operations_dict:
        print(i)
    contiue_flag = True

    while contiue_flag:
        op_symbol = (input("select operation:-"))
        number2 = float(input("Enter a second number:-"))
        calculator_function = operations_dict[op_symbol]
        output = calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2}={output}")
        should_continue = input(
            f"Enter y to continue calculation with {output} or n to star to new calculation or x to exit").lower()
        if should_continue == 'y':
            number1 = output
        elif should_continue == 'n':
            contiue_flag==False
            os.system('cls')
            calculator()

        else:
            contiue_flag = False
            print("Bye Have a good day")

calculator()

