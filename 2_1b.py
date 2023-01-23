sum =0
for i in range (1,100,1):
    ino =  (input('Enter a number or e to exit the program: ')) 
    if ino == 'e':
        break
    elif int(ino)>0 and int(ino) < 100:
        sum += int(ino)
print ('The sum of your inputs is: ',sum)
