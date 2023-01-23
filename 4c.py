d = int(input('Enter your college credits: '))
if d >=90:
    print('Senior Status')
elif d<90 and d>=60:
    print('Junior Status')
elif d<60 and d>=30:
    print('Sophomore Status')
else:
    print('Freshman Status')