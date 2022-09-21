from art import logo

print(logo)


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def sub(n1, n2):
    return n1 - n2


# Multiply
def mul(n1, n2):
    return n1 * n2


# Divide
def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    num1 = float(input("What's the first number?: "))

    next_iteration = True

    while next_iteration:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick the operation from the line above: ")

        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            next_iteration = False
            calculator()


calculator()
