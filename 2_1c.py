sum =0
while True:
    ino =  (input('Enter a number or e to exit the program: ')) 
    if ino == 'e':
        break
    elif int(ino)>0 and int(ino) < 100:
        sum += int(ino)
    else:
        continue
print ('The sum of your inputs is: ',sum)
