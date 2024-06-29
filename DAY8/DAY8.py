# Caesar Cipher------------------------------------------------------------------------------------
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"


    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).

shift = shift % 26

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
if restart == "no":
    should_end = True
    print("Goodbye")





# def my_function(something)-----------------------------------

# if:def my_function(123)
# something = Parameter (參數名稱) ；  123 = Argumet (實際數據)
#
# def greet():
#     print("Hello ")
#     print("How do you do ")
#     print("So happy to see you, ")
#
# #Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
# greet_with_name("angel")


# Function with more than 1 input ()------------------------------------------
#if def my_function(a, b)
#(a, b) = position argument 位置參數 位置不可變更(a對1，b對2的位置)

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"what is it like in {location}?")
#
# greet_with("angel", "a3")
# greet_with("a3", "angel")

#keyword arguments(運作時，若在()內將參數=argument 即便位置變更，對應的Parameter也不會變--------------

#if def my_function(a, b) , my_function(b="2", a="1")
# def greet_with_key(name, location):
#     print(f"Hello {name}")
#     print(f"what is it like in {location}?")
#
# greet_with_key(location="a3", name="angel")



# Caesar Cipher------------------------------------------------------------------------------------


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt (plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
#     # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     # e.g.
#     # plain_text = "hello"
#     # shift = 5
#     # cipher_text = "mjqqt"
#     # print output: "The encoded text is mjqqt"
#
#     ##HINT: How do you get the index of an item in a list:
#     # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#
# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# encrypt (plain_text=text , shift_amount=shift)
#
#
# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#
# def decrypt (cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The encoded text is {plain_text}")
#
#
#   #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#   #e.g.
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print output: "The decoded text is hello"
#
#
# #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == 'encode':
#     encrypt (plain_text=text , shift_amount=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text, shift_amount=shift)

#
# #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == 'decode':
#             shift_amount *= -1
#     for letter in start_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     print(f"The {cipher_direction}d text is {end_text}")
#
# #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)