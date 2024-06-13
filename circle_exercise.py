class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def get_circumferance(self):
        return self.pi*self.radius
    def area_circle(self):
        return self.pi*self.radius*self.radius
circle_1=circle(5)
print(circle_1.get_circumferance())
circle_2=circle(12)
print(circle_2.area_circle())


