password_lookup ={} #empty dictionary 
while True:
    key = input('Enter your username: or z to exit: ')
    if key =='z':
        break
    assciated_string = input('Enter your password: ')
    password_lookup[key] = assciated_string
print (password_lookup)
