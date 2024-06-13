roll_no={
    'avishkar':35,
    'ajay':35,
    'ram':65,
    'akshay':97,
}
print(roll_no)
print(roll_no['ajay'])
roll_no['avishkar']=5654
print(roll_no)
roll_no.pop('avishkar')
print(roll_no)
roll_no['avishkar']={'work_place':123456,'home':456789,'normal':369852}
print(roll_no.keys())
#roll_no.clear()
print(roll_no.items())

