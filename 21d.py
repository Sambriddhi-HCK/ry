positive = 0
negative = 0
bool = False
while ( not bool):
    check = (input('Enter a number or e to exit the program: ')) 
    if check == 'e':
        break
    else:
        if int(check) >0 :
            positive+=1
        elif int(check)<0:
            negative+=1
        else:
            continue
print (' The number of positive numbers entered is: ', positive, '\nThe number of negative numbers enterewd is : ', negative)
