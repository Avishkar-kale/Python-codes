class human:
    def __init__(self):
        self.nose = 1
        self.eyes = 2
        print("calling init from human")
        self.language = 'python'

    def work(self):
        print("i can work")
class male:
    def __init__(self, name):
        self.name = name
        print("call init from male")


    def eat(self):
        print("i can eat")



    def work(self):
        print("i can code")

class boy(human, male):
    def __init__(self, name):
        super().__init__()
        male.__init__(self, name)
    def work(self):
        print("i can test the code")


boy_1 = boy('Avishkar')
male.work(boy_1)
boy_1.work()
human.work(boy_1)
print(boy_1.eyes)
print(boy_1.name)
print(boy_1.language)