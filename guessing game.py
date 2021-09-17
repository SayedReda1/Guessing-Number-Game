from random import randint
from pyfiglet import figlet_format

answer_num = randint(0, 11)
chances = 4
count = 0

user_answer = int(input(
    f"Start Game !\nI'm thinking of a number between 0 and 10\nYour mission is to guess it\nYou have 5 chances\nGo !!\nYour Guess: "))
# When The Input Is Wrong
while answer_num != user_answer:
    print("\n")

    # Alert For The Last Chance
    if count == (chances - 1):
        print("Be Careful, This is your last chance")
    # Afer The Last Chance Is Wrong
    if count == chances:
        print(figlet_format("YOU LOSE"))
        break
    # The Wrong Number And Hint Message
    if (count < chances - 1) and (answer_num > user_answer):
        print(
            f"Wrong number, {chances - count} chances left\n[HINT]: Try a higher number")

    if (count < chances - 1) and (answer_num < user_answer):
        print(
            f"Wrong number, {chances - count} chances left\n[HINT]: Try a lower number")
    count += 1

    user_answer = int(input("\nYour answer: "))


if answer_num == user_answer:
    print(figlet_format("YOU WIN"))
