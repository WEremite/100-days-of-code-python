from art import logo, vs
from game_data import data
import random


def get_random_data():
    return random.choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


def game():
    print(logo)
    points = 0
    right_answer = True
    account_a = get_random_data()
    account_b = get_random_data()

    while right_answer:
        account_a = account_b
        account_b = get_random_data()

        while account_a == account_b:
            account_b = get_random_data()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(user_guess=guess, a_followers=a_follower_count, b_followers=b_follower_count)

        if is_correct:
            points += 1
            print(f"You're right! Current points: {points} points.")
        else:
            right_answer = False
            print(f"Sorry, that's wrong! Final points: {points} points.")


game()
