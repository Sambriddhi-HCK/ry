def caesar_cipher(message, shift, operation):
    '''Encrypts or decrypts the message by shifting each letter by the given shift.'''
    result = ''
    for char in message:
        if char.isalpha():
            if operation == 'encrypt':
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                shifted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result += shifted_char
        else:
            result += char
    return result
print('Welcome to Caesar Cipher ')
print('This program encrypts and decrypts text using Caesar Chiper. ')

while True:
    operation = input('Would you like to encrypt (e) or decrypt (d): ')
    if operation.lower() not in ['e', 'd']:
        print("Invalid input. Please enter 'e' to encrypt or 'd' to decrypt.")
        continue

    message = input('What message would you like to {}: '.format(operation))
    shift = int(input('What is the shift number: '))

    if operation.lower() == 'e':
        operation = 'encrypt'
    else:
        operation = 'decrypt'

    print(caesar_cipher(message, shift, operation))

    again = input('Would you like to encrypt or decrypt another message? (y/n): ')
    if again.lower() != 'y':
        print('Thanks for using the program, goodbye!')
        break