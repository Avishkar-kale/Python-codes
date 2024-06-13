import random
import logo_art

EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(choosen_level):
    if choosen_level=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif choosen_level=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return



def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("your guess is to low")
        return attempts-1
    elif(guessed_number>answer):
        print("your guess is to high")
        return attempts-1
    else:
        print(f"you guess {answer} is right.. ")


def game():
    print(logo_art.logo)
    print("Let me think of number between 1to50:..")
    answer = random.randint(1, 50)
    level = input("choos level of dificulty easy or hard: ")
    attempts = set_difficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("you have enterd wrong difficulty level play again...!")
        return
    guessed_number = 0
    while guessed_number != answer:
        print(f"you have {attempts} remaining attempts guess the number")
        guessed_number = int(input("guess a number:"))
        attempts = check_answer(guessed_number, answer, attempts)
        if attempts == 0:
            print("you are out of guess...You lose the game")
            return
        elif guessed_number!=answer:
            print("guess again")

game()



