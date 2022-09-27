from random import randint
from colorama import Fore

answer_num = randint(0, 10)
chances = 3

print(f"Start Game !\nI'm thinking of a number between 0 and 10\nYour mission is to guess it\nYou have {chances} chances\nGo !!")

while chances > 0:
    user_answer = int(input(Fore.WHITE + "\nYour answer: "))

    # Winning message
    if user_answer == answer_num:
        print(Fore.GREEN + "YOU WIN :) ")
        break
    # The Wrong Number And Hint Message
    elif (user_answer > answer_num):
        print(Fore.RED + "Wrong number")
        print(Fore.YELLOW + "[HINT]: Try a lower number")
    elif (user_answer < answer_num):
        print(Fore.RED + "Wrong number")
        print(Fore.YELLOW + "[HINT]: Try a higher number")
    chances -= 1

    # printing the remaing chances
    if chances == 1:
        print(Fore.YELLOW + "Be Careful, This is your last chance")
    else:
        print(Fore.YELLOW + f"{chances} chances left")

if chances == 0:
    print(Fore.RED + "YOU LOSE")
