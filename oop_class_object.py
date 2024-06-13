class Instructor:
    def __init__(self,name,address):
        self.name=name
        self.address=address

Instructor_1=Instructor('Avishkar','Pune')
print(Instructor_1.name)
print(Instructor_1.address)

class Instructor_1:
    def __init__(self,job,mobile_no,car):
        self.job1=job
        self.mobile_no=mobile_no
        self.car=car

instructo_3=Instructor_1('cloud_engineer','123456789','BMW')
print(instructo_3.job1)
print(instructo_3.mobile_no)
print(instructo_3.car)
