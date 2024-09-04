# Title: Caesar Cipher - Encode
# Author: Mr Friend
# Date: 30 Sep 2022

# Declare global variables
plainText = ""
key = 0
interimText = ""
letterValue = 0
cipherText = ""

# Get plain text message
plainText = input("Plain text: ")

# Get valid key value
key = int(input("Key: "))

# Input validation
while key < 1 or key > 25:
    # Display error message
    print("Key must be between 2 and 25")
    # Get valid key value
    key = int(input("Key: "))

# Loop