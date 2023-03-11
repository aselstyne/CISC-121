# Name:   Alex Aselstyne
# Student Number: 20289805
# Email:  alex.aselstyne@queensu.ca

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity


# Vigenere Encryption

def make_alpha(plain):
    ''' make_alpha strips all non-alphabetical characters from the 
    specified string '''
    index = 0
    while (index < len(plain)):
        if (plain[index].isalpha() == False):
            plain = plain[:index]+plain[index+1:]
        else:
            index = index+1
    return plain


# Get input from the user (plaintext and key)
plaintext = input("Please input your plaintext to be encrypted: ")
key = input("Now input your key: ")


# Convert plaintext and key to all upper case letters 
plaintext = plaintext.upper()
key = key.upper()


# Remove all non-letters from plaintext and key
plaintext = make_alpha(plaintext)
key = make_alpha(key)
        

# Encrypt plaintext
encrypted = ''
for i in range(len(plaintext)):
    key_val = ord(key[i%len(key)]) - 65 # Subract 65 so A is 0
    text_val = ord(plaintext[i]) - 65
    # Adding the two vals gives you the value for the encrypted character,
    # but the mod 26 is there for overflow past z.  Add 65 to get ASCII again.
    combo = (key_val + text_val)%26 + 65
    encrypted = encrypted + chr(combo)


# Show result on screen
print(encrypted)