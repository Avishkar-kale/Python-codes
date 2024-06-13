class Inheritance:
    def __init__(self,address):
        self.nose=1
        self.eyes=2
        self.address=address

    def eat(self):
        print("i can it")
    def work(self):
        print("I can work")
    def walk(self):
        print("I can walk")

class Male(Inheritance):
    def __init__(self,name,address):
        super().__init__(address)
        self.name=name
        self.address=address
    #Here is Inheritance is parent class and now Male class access the all attribute that present in INheritance class
    def male(self):
        print("My gender is male")
    def work(self):
        super().work()  #now here is the example of super() function this function is very useful when same function defined in parent class and child class
                         #withot super() function we can not access easily with the help of super function we can access easily
        print("I can write code")

inheritance_1=Inheritance('pune')
inheritance_1.eat()
inheritance_1.work()

male_1=Male('Avishkar','pune')
male_1.male()
male_1.work()
print(male_1.nose)
print(f"i have {male_1.eyes} eyses")
print(male_1.name)
print(male_1.address)

