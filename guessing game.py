from random import *
from typing import Type
from pyfiglet import *
from termcolor import *
answer_num = randint(0, 11)
print(answer_num)
chances = 4
count = 0

user_answer = int(input(
    f"Start Game !\nI'm thinking of a number between 0 and 10\nYour mission is to guess it\nYou have {chances} chances\nGo !!\nYour Guess: "))
while answer_num != user_answer:
    print("\n")
    count += 1

    if count == chances:
        print("Be Careful, This is your last chance")
    if count > chances:
        print(figlet_format("SORRY YOU LOST"))
        break

    if (count < chances) and (answer_num > user_answer):
        print(
            f"Wrong number, {chances - count} chances left\n[HINT]: Try a higher number")

    if (count < chances) and (answer_num < user_answer):
        print(
            f"Wrong number, {chances - count} chances left\n[HINT]: Try a lower number")
    user_answer = int(input("\nYour answer: "))


if answer_num == user_answer:
    print(figlet_format("YOU WIN"))

# ------------------------------------------------------------------------


# ------------------------------------------------------

# secret_number = randint(1, 11)
# # print(secret_number)
# print("                 Start!\nI'm thinking of a number between 1 and 10\n       your mission is to find it\n")
# user_entry = int(input("What number do think of ? "))
# limit = 2
# count = 0
# out_of_chances = False
# while user_entry != secret_number and not out_of_chances:
#     print(f"Wrong Number, {limit - count} chances left\n")

#     if count < limit:
#         user_entry = int(input("Type your guess: "))
#         count += 1
#     else:
#         out_of_chances = True

# if out_of_chances:
#     print(figlet_format("SORRY YOU LOST "))
# else:
#     print(figlet_format("YOU WIN ! "))
