# ------------------------------------------------------------------------------------------------------------------------------------
# Name: Shivam Janda
# Date: October 8, 2022
# Program: SYSA-3204
# Description: This program generates a random secure password that has to be greater or equal than 8 characters.
# The user can enter the specific amount of letters, special characters and digits they want within the range of the length of password
# they have entered. Output the random letters, special characters and digits in random order to the user.
# ------------------------------------------------------------------------------------------------------------------------------------
import random
import string

print("Random Password Generator")

passLength = int(input("Enter the length of the password: ")) # Ask user for input for the length of the password they want and convert to a integer

while passLength < 8:  # keep looping until the user enters a input that is greater or equal to 8
    print("Please enter a value of greater than or equal to 8 to create a secure password")  # validation error
    passLength = int(input("Enter the length of the password "))  # re ask for the input

passLetters = int(input("Enter the number of letters desired in the password: "))  # if passed the while loop above then ask for the number of letters input

while (passLetters < 0) or (passLetters > passLength):  # keep looping if the user inputs the amount of letters is less than zero or greater than the length of the password
    print("The number of letters should be in the range of 0 and", passLength)  # validation error
    passLetters = int(input("Enter the number of letters desired in the password: "))  # re ask for the input

randomLetter = random.choices(string.ascii_letters, k=passLetters)  # once the number of proper password letter input is set then randomly generate letters based of how many random letters the user wanted

passDigits = int(input("Enter the number of digits desired in the password: "))  # if passed the while loop above then ask for the number of digits input

while (passDigits < 0) or (passDigits > passLength - passLetters):  # keep looping if the user inputs the amount of digits is less than zero or greater than the length of the amount of characters left for the new password
    print("The number of digits should be in the range of 0 and", passLength - passLetters)  # validation error
    passDigits = int(input("Enter the number of digits desired in the password: "))  # re ask for the input

randomDigits = random.choices(string.digits, k=passDigits)  # once the number of proper password digits input is set then randomly generate digits based of how many random digits the user wanted

passSpecial = int(input("Enter the number of special characters desired in the password: "))  # if passed the while loop above then ask for the number of special characters input

while (passSpecial < 0) or (passSpecial > passLength - passLetters - passDigits):  # keep looping if the user inputs the amount of special characters is less than zero or greater than the length of the of characters left for the new password
    print("The number of special characters should be in the range of 0 and", passLength - passLetters - passDigits)  # validation error
    passSpecial = int(input("Enter the number of special characters desired in the password: "))  # re ask for the input

randomSpecial = random.choices(string.punctuation, k=passSpecial)  # once the number of proper password special characters input is set then randomly generate special characters based of how many random special characters the user wanted

addTogether = randomLetter + randomDigits + randomSpecial # add all the randomly generated values together into one string

listString = list(addTogether)  # add the characters of the string into a list
random.shuffle(listString)  # shuffle all the characters
password = ''.join(listString)  # put the randomly shuffled characters into a new string

print("Your desired password is: ")
print(password)  # output password to user


