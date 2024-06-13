class Human:
    def __init__(self,name,age):
        print("calling init from Human")
        self.name=name
        self.age=age
    def eat(self):
        print("i can it")


class Male(Human):
    def __init__(self,name,age,location):
        super().__init__(name,age)
        self.location=location
    def sleep(self):
        print("I can sleep whole day")


class Female(Human):
    def __init__(self,name,age):
        print("Calling init from Female")
        super().__init__(name,age)
    def work(self):
        print("i can work")

male_1=Male('Avishkar',19,'Pune')
male_1.sleep()
male_1.eat()
print(male_1.name)
print(male_1.age)
female_1=Female('Ajay',20)
female_1.work()
print(female_1.name)