# check if number is prime
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


user_pick = int(input("Please, write any number: "))
prime_checker(number=user_pick)
