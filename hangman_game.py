import random
word_list = ['hello','wod','programming','python','machine learning','artificial intelligence','data_science','cloud computing','big_data','the future']
lives=6
display =[]
choosen_word = random.choice(word_list)
#print(choosen_word)
for word in range(len(choosen_word)):
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed_letter = input(f'guess a letter:\n you have only {lives} chance to guess the letter').lower()
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if guessed_letter==letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in choosen_word:
        lives -=1
        if lives == 0:
            game_over=True
            print('you lose the game')
    if '_' not in display:
        game_over=True
        print("you win the game")
