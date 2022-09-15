import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
print("Welcome to Rock, Paper, Scissors game!")
user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))
computer_pick = random.randint(0, 2)


def show_pick(pick):
    if pick == 0:
        print(rock)
    elif pick == 1:
        print(paper)
    else:
        print(scissors)


show_pick(user_pick)
print("Computer chose:")
show_pick(computer_pick)

if user_pick == computer_pick:
    print("It's a draw.")
elif (user_pick == 0 and computer_pick == 1) or (user_pick == 1 and computer_pick == 2) or \
        (user_pick == 2 and computer_pick == 0):
    print("You lose!")
else:
    print("You win!")
