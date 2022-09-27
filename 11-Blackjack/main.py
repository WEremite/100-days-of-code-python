from art import logo
import random

print(logo)


def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(list_of_cards):
    sum_of_cards = sum(list_of_cards)
    ace_count = list_of_cards.count(11)
    if len(list_of_cards) == 2 and sum_of_cards == 21:
        return 0

    if sum_of_cards > 21 and ace_count > 0:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        return sum(list_of_cards)

    return sum_of_cards


def compare(user_points, computer_points):
    if user_points == 0:
        print(f"Your score is 21! Computer's score is {computer_points}. You win!")
    elif computer_points == 0:
        print(f"Computer's score is 21! Your score is {user_points}. You lose!")
    elif user_points > 21 or user_points < computer_points:
        print(f"Your score is {user_points}! Computer's score is {computer_points} {computer_cards}. You lose!")
    elif computer_points > 21 or user_points > computer_points:
        print(f"Your score is {user_points}! Computer's score is {computer_points} {computer_cards}. You win!")
    else:
        print(f"Your score is {user_points}! Computer's score is {computer_points} {computer_cards}. It's draw!")


def game():
    user_cards.append(deal())
    if calculate_score(computer_cards) < 17:
        computer_cards.append(deal())
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards are: {user_cards}, your score: {user_score}.")
    print(f"Computer's first card is: {computer_cards[0]}.")
    next_turn = input("Would you like to pick another card? (y/n): ")
    if next_turn == "n":
        compare(user_points=user_score, computer_points=computer_score)
    else:
        game()


# user_cards = [deal()]
# computer_cards = [deal()]

ready_for_game = True
while ready_for_game:
    user_choice = input("Would you like to play the game? (y/n): ")
    if user_choice == "y":
        user_cards = [deal()]
        computer_cards = [deal()]
        game()
    else:
        ready_for_game = False
