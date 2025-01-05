from art import cypher_logo

print(cypher_logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

on = True

while on:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(start_text, shift_amount, cypher_direction):
        end_text = ""
        if cypher_direction == "decode":
            shift_amount *= -1
        for letter in start_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        print(f"The {direction}d text is '{end_text}'. \n")


    caesar(start_text=text, shift_amount=shift, cypher_direction=direction)

    restart = input("Would you like to restart? Type 'yes' or 'no': ").lower()

    if restart == "yes":
        on = True
    else:
        on = False
