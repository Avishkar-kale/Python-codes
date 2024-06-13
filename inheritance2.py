class Human:
    def __init__(self,qualification):
        self.name='Avishkar'
        self.add='pune'
        self.qualification=qualification
class Male(Human):
    def __init__(self,clg,qualification):
        super().__init__(qualification)
        self.eye=2
        self.nose=2
        self.clg=clg




m1=Male('BCA','Sinhagad')
print(m1.clg)
print(m1.qualification)
print(m1.name)
h1=Human("BCA")
print(h1.add)
print(h1.name)
