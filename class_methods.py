class Instructor:
    followers=0  # is it class variable
    def __init__(self,name,address,course):
        self.name=name
        self.address=address
        self.course=course
        #print(f"My name is {name}")
    def display(self,course):
        print('Hey this is the example of methods')
        print(f'hii my name is {self.name} and i tech you {self.course}')

instructor_1=Instructor('Avishkar kale','pune','Python')
print(instructor_1.name)
print(instructor_1.address)
print(instructor_1.course)
#print(instructor_1.display()) #this is the example of how to add and call methods
#print(instructor_1.followers)  #this followers get default value
instructor_1.display('Python')

