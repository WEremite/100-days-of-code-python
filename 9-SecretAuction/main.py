from os import system
from art import logo

print(logo)

print("Welcome to Secret Auction!")

participants = {}
another_participant = True


while another_participant:
    name = input("What is your name? ").title()
    bid = int(input("What is your bid? $"))

    participants[name] = bid

    another_bid = (input("If there another_participant? (Type 'yes' or 'y' to continue /"
                         " 'no' or 'n' to cancel) ")).lower()

    if another_bid == "yes" or another_bid == "y":
        pass
    else:
        another_participant = False
    system("clear")

max_bit_name = max(participants, key=participants.get)

print(f"The winner is {max_bit_name} with {participants[max_bit_name]}$ bit.")
