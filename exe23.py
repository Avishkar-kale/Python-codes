student_marks={
    'Ajay':98,
    'Govind':97,
    'Shantanu':100,
    'avishkar':95,
    'Ram':100,
    'shyam':100,
    'ramesh':45,
    'rajesh':65,
    'Muktesh':75,
    'Atul':55,
}
student_grade={}
#print(student_marks.keys())
for student in student_marks:
    marks = student_marks[student]
    if marks>90:
        student_grade[student] ='A+'
    elif marks>85:
        student_grade[student] = 'A'
    elif marks>60:
        student_grade[student] = 'B'
    elif marks>40:
        student_grade[student] = 'c'
    elif marks==40:
        student_grade[student] = 'd'
    else:
        student_grade[student]='you are fail'


print(student_grade)


