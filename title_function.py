def formated_name(f_name,l_name):
    formated_fname = f_name.title()
    formated_lname = l_name.title()
    if f_name=='' and l_name=='':
        return 'Please enter valid input'
    else:
        return f"{formated_fname},{formated_lname}"


f_name=input('Enter your name')
l_name=input('Enter your last name')
reasult=formated_name(f_name,l_name)
print(reasult)