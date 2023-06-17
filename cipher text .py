def validate_key(plainText, key):
    """
    Validate the given key to be suitable for Vigenere cipher
    """
    key_len = len(key)
    if key_len < len(plainText):
        # Repeat the key until it's the same length as the plaintext
        repeats_needed = len(plainText) // key_len + 1
        key = (key * repeats_needed)[:len(plainText)]
    elif key_len > len(plainText):
        # Trim the key if it's longer than the plaintext
        key = key[:len(plainText)]
    return key

def removeNonAlpha(text):
    """
    Remove all non-alphabetic characters from the given text
    """
    return ''.join(c for c in text if c.isalpha())

def encrypt(plainText, key):
    """
    Encrypt plaintext using Vigenere cipher and key
    """
    cipherText = ""
    plainText = removeNonAlpha(plainText).upper()  # Remove non-alphabetic characters and convert to uppercase
    key = removeNonAlpha(key).upper()  # Remove non-alphabetic characters from the key
    
    key = validate_key(plainText, key)  # Make sure the key is the same length as the plaintext
    
    for i in range(len(plainText)):
        char = plainText[i]
        keyChar = key[i]
        charIndex = ord(char) - 65
        keyIndex = ord(keyChar) - 65
        cipherIndex = (charIndex + keyIndex) % 26
        cipherChar = chr(cipherIndex + 65)
        cipherText += cipherChar
    
    return cipherText




plaintext = input("Please Insert Plaintext : ")
key =input("Please Insert the KEY: ")
cipher_text = encrypt(plaintext, key)
print(cipher_text)
