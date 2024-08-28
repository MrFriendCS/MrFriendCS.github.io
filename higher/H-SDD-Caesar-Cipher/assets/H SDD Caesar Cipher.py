# Title: Caesar Cipher
# Author: Mr Friend
# Date: 4 Dec 2019

def encode(plaintext, key):
    # Declare local variables
    asciiValue = 0
    ciphertext = ""
    
    # Encrypt the message
    plaintext = plaintext.lower() # Change the message to lower case

    for letter in plaintext:
        asciiValue = ord(letter) # Convert letter to ASCII code
        
        if asciiValue >= 97 and asciiValue <= 122: # Only encrypt a to z
            asciiValue = asciiValue + key
            
            if asciiValue > 122: # If past z
                asciiValue = asciiValue - 26
            
            ciphertext = ciphertext + chr(asciiValue) # Convert ASCII code to letter
        
        else:
            ciphertext = ciphertext + letter
        
    return ciphertext

def decode(ciphertext, key):
    # Declare local variables
    asciiValue = 0
    plaintext = ""
    
    # Decrypt the message
    ciphertext = ciphertext.lower() # Change the message to lower case

    for letter in ciphertext:
        asciiValue = ord(letter) # Convert letter to ASCII code
        
        if asciiValue >= 97 and asciiValue <= 122: # Only encrypt a to z
            asciiValue = asciiValue - key
            
            if asciiValue < 97: # If past z
                asciiValue = asciiValue + 26
            
            plaintext = plaintext + chr(asciiValue) # Convert ASCII code to letter
        
        else:
            plaintext = plaintext + letter
        
    return plaintext



# Declare variables
temp = ""
encrypt = True
messageCount = 0
key = 0
inputText = ""
outputText = ""

# Encode or decode
temp = input("Encode? (Yes/No): ")

if len(temp) > 0:
    encrypt = temp[0].lower() == "y"

# How many messages
while messageCount < 1:
    temp = input("How many messages? ")
    if temp.isnumeric():
        messageCount = int(temp)

# Loop for the number of messages
for counter in range(messageCount):
    
    # Get the cipher key
    while key < 1 or key > 25:
        temp = input("Enter the key: ")
        if temp.isnumeric():
            key = int(temp)
    
     # Get plaintext   
    inputText = input("Enter your message: ")
    
    if encrypt:
        outputText = encode(inputText, key)
    else:
        outputText = decode(inputText, key)

    print(outputText)
    outputText = "" # Destroy the evidence!
