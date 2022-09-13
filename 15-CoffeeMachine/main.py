MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True if the resources are sufficient for the order or False otherwise"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, is not enough {item}!")
            return False
    return True


def process_coins():
    """Returns the total amount of coins inserted by the customer"""
    print("Please, insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dines?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True if the customer has enough money to buy the drink or False otherwise"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money!")
        return False


def make_drink(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Your {drink_name} is ready! Enjoy! ☕️")


is_on = True

while is_on:
    choice = input("What do you want to buy? (espresso, latte, cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"The coffee machine has:")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])
