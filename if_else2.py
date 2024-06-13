name = input('Enter your Name')
age = int(input('enter your age'))
if age == 5:
    print(f'hey {name} no need to by token..')
elif age >5 and age <= 18:
    print(f' hey {name} you need to by token and you need to pay 250')
elif age >18 and age<=40:
    print(f'hey {name} you need to pay 500')
elif age > 40 or age >60:
    print(f'sorry {name} you can not get token ... Thank You')
else:
    print(f'hey {name} sorry you can not ride you are so small Tahnk You__')


