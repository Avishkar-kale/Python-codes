

#THIS EXAMPLE IS KWARGS OR KEYWORD_ARBITARY FUNCTION EXAMPLE
def info_person(*NUM,**info):
    for key, value in info.items():
        print(key,value)#we can use hear any name or letter liki i and j
        print(NUM)

info_person(1,2,3,4,5,name='avishkar', dept='computer science')
info_person(name='avishkar',dept='computer science',Mno=7498408094)
