from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '.', ',', '?', '!', '-', '+', '\'']

print(logo)


def caesar(plain_text, shift_amount, task):
    result = ""
    if task == "decode":
        shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
            shifted_index = (alphabet.index(char) + shift_amount)
            result += alphabet[shifted_index % len(alphabet)]
        else:
            result += char

    print(f"Ba-dooms! And some magick happened! Your {task}d text is: {result}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction != "encode" or direction != "decode":
        print("Good luck next time...")
        break

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(plain_text=text, shift_amount=shift, task=direction)

    again = input("Type 'yes' if you want to start again. Otherwise type 'no' or anything.\n")
    if again != "yes":
        should_continue = False
        print("Good bye!")
