
#POSITIONAL ARGUMENTS
def info(name,dept):
    print(f"hii {name}")
    print(f"you are form {dept}")

info('avishkar','cs')

#keyword Argument..........

def info(name,dept):
    print(f"hii {name}")
    print(f"you are form {dept}")

info(dept='Computer science',name='Avishkar')

#Default Arguments.............................

def info(name,dept,sub='python'):
    print(f"hii {name}")
    print(f'now you lerning {sub}')
    print(f"you are form {dept}")

info('avishkar','cs')


#Parametere lenght variable............................

def add(*number):
    c=0
    for i in number:
        c = c + i
    print(c)

add(1,1,5,8,9,7,4,1,2,3,6,9,8,5,2,5)


