class Class1:
    def __init__(self,name,age):
        self.__name=name
        self._age=age
    def work(self):
        print('Now currently i work in oracle')
    def get_age(self):
        return self._age
    def set_age(self,age):
        if age>35:
            print('please enter valid age')
        else:
            print(age)

c1=Class1('Krishna',10)
#print(c1._age)
#print(c1.__name)
print(c1.get_age())
c1.set_age(30)