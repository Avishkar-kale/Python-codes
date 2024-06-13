class human:
    def __init__(self,heart):
        self.eyes = 2
        self.nose = 1
        self.heart = heart
    def eat(self):
        print("i can it")
    def work(self):
        print("i can work")

class male(human):
    def __init__(self,name):
        self.name = name
    def sleep(self):
        print("i sleep whole day")
    def work(self):
        print("i can write the code")

class boy(male):
    def __init__(self,language,heart,name):
        self.language = language
        human.__init__(self,heart)
        male.__init__(self,name)
    def programmer(self):
        print("i test codes of any language")
    def developer(self):
        print("I am developer")

boy_1 = boy('Java',1,'Avishkar')
boy_1.eat()
print(boy_1.eyes)
print(boy_1.nose)
print(boy_1.heart)
print(boy_1.language)
print(boy_1.name)