# Random Password Generator

# Import required modules
import random
import string

# ---------------------------------------------
# USER INPUT
# ---------------------------------------------

# Ask user for password length
length = int(input("Enter password length: "))

# ---------------------------------------------
# CHARACTERS FOR PASSWORD
# ---------------------------------------------

# Combine:
# - Uppercase letters
# - Lowercase letters
# - Numbers
# - Special characters

characters = (
    string.ascii_letters +   # a-z + A-Z
    string.digits +          # 0-9
    string.punctuation       # Special symbols
)

# ---------------------------------------------
# GENERATE PASSWORD
# ---------------------------------------------

password = ""

# Loop runs according to user length
for i in range(length):

    # Select random character
    random_char = random.choice(characters)

    # Add character to password
    password += random_char

# ---------------------------------------------
# OUTPUT
# ---------------------------------------------

print("\nGenerated Password:")
print(password)