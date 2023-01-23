#This program encrypts and decrypts the given message according to Caeser Cipher
def main():
    '''This function is the main, which calls other methods. '''
    welcome()
    while True:
        mode_of_conversion = enter_message()
        if mode_of_conversion == 'd':
            decrpyt()
        else:
            encrypt()
        another = ''
        while another.lower() not in ('y','n'):
            another = input(('Would you like to encrpyt or decrpyt nother message? Please enter y if yes and n if no: ').lower())
        if another.lower() == 'n':
            print('Thanks for using the program, goodbye!')
            break

def welcome():
    '''This funnction prints an introduction to the user.'''
    salutation = 'Welcome to the Caesar Cipher \nThis program encrypts and decrypts message with the Caesar Cipher.'
    print(salutation)

def enter_message():
    '''This function returns the selected mode of conversion by the user. Moreover, the input is converted to lower case to avoid errors in the program'''
    while True:
        mode_of_conversion = input(('Would you like to encrypt(e) or decrypt(d): ').lower())
        if (mode_of_conversion == 'e' or mode_of_conversion == 'd'):
           break
        else:
            print ('Invalid Mode\n')
            continue
    return mode_of_conversion

def encrypt():
    '''This function converts the message into upper case and encrpyts the guser given message according to the entered shift'''
    message = list(input('What message would you like to encrypt: \n').upper())
    while True:
        shift_number = int (input('What is the shift number: '))
        if shift_number == int(shift_number):
            break
        else:
            print('Invalid Shift')
    encrypted =""
    for le in range(len(message)):
        letter = message[le]
        if letter == ' ':
            shifted_text =' '
        else:
            shifted_text = chr((ord(letter)+ shift_number - 65)% 26 + 65)
            encrypted+=shifted_text
    print(encrypted)
    return message, shift_number

def decrpyt():
    '''This function converts the message into upper case and decrpyts the given message acording to the entered shift'''
    message = list(input('What message would you like to decrypt:  \n').upper())

    while True:
        shift_number = int (input('What is the shift number: '))
        if shift_number == int(shift_number):
            break
        else:
            print('Invalid Shift')
    decrpyted =""
    for ler in range(len(message)):
        letter = message[ler]
        if letter == ' ':
            shifted_text =' '
        else:
            shifted_text = chr((ord(letter)- shift_number - 65)% 26 + 65)
            decrpyted +=shifted_text
    print(decrpyted)
    return message, shift_number

if __name__ == '__main__':
    main()