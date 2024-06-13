def display():
    print(f"here we create gobal variablr with the help of global keyword")
    global a
    a=20
    print(f"this value inside the function:={a+20}")
display()
print(f"this value is outside the function cause we create gobal variable with the help of global keyword:={a}")