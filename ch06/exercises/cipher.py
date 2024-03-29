#import turtle

import random

def my_cipher(text, shift):
    """
    Encrypts a message using a custom substitution cipher.

    args:
        text:str = the message to encrypt
        shift:int = the number of positions to shift each alphabetic character
    return:
        :str = the encrypted message
    """
    

    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the new position of the character after the shift
            new_pos = (ord(char) - start + shift) % 26
            # Convert the new position back to a character
            char = chr(start + new_pos)
        result += char
    return result



#message = input("enter a message: ")
message = "The quick brown fox jumps over the lazy dog"
shift = random.randint(1,10)
encrypted_message = my_cipher(message, shift)

with open("c:/Users/aakha/github-classroom/bucs110SPRING23/portfolio-akh90/ch06/exercises/encrypted.txt", "w") as file:
    file.write(encrypted_message)
    file.close()
