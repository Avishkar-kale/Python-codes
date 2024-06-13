
import random
count = 0
ch_list = ['A','a', 'B', 'b' 'C', 'c', 'D', 'd', 'E','e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j',
'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's','T', 't', 'U', 'u',
'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number_list = ['1','2','3','4','5','6','7','8','9','10']
symbol_list = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@']
password_list=[]
print("𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙏𝙃𝙀 𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿 𝙂𝙀𝙉𝙍𝙀𝙏𝙀𝙍")
charcter =int(input("how many charcter you want to in your password?: "))
number = int(input("how many number you want to in your password?: "))
symbol = int(input("how many symbol you want to in your password?: "))
for i in range(1,charcter+1):
   char = random.choice(ch_list)
   password_list += char
for i in range(1,number+1):
   char = random.choice(number_list)
   password_list += char
for i in range(1,symbol+1):
    char = random.choice(symbol_list)
    password_list += char
#print(password_list)
random.shuffle(password_list)
#print(password_list)
password=""
for char in password_list:
    password += char
print(password)



