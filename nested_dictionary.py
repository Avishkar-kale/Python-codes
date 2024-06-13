student_data=[
    {'name':'ram','roll_no':30,'age':20,'course':'python'},
     {'name':'dinesh','roll_no':35,'age':22,'course':'java'},
    {'name':'athrva','roll_no':40,'age':18,'course':'c++'},

]
print(student_data)
def new_student(name,rollno,age,course):
    new_data={}
    new_data['name']=name
    new_data['roll_no']=rollno
    new_data['age']=age
    new_data['course']=course
    student_data.append(new_data)
new_student('shyam',32,20,'javascript')

print(student_data)