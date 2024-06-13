class Human:
    def __init__(self,name):
        self.eyes = 2
        self.nose = 1
        self.name = name
    def eat(self):
        print('i can it')


class Male:
    def __init__(self):
        self.language = 'Python'
        # self.Ql = Ql
    def flirt(self):
        print('I can flirt')


class Boy(Human, Male):
    def __init__(self,add,name):
        Human.__init__(self,name)
        # Male.__init__(self,Ql)
        self.add = add


h1 = Human('Avishkar')
m1 = Male()
b1 = Boy('Pune','Avishkar')
b1.eat()
print(b1.eyes)
print(b1.nose)
print(b1.eat)
print(b1.name)
print(b1.flirt())
# print(b1.Ql)
