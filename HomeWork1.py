age = int(input('Введите свой возраст: '))
if age < 6:
    print('Детсадовец')
elif ( age >= 7 ) and ( age < 16):
    print('Школьник')
elif ( age >= 17 ) and ( age < 25 ):
    print('Студент')
elif ( age >= 26 ) and ( age < 60 ):
    print('Работяга')
elif ( age >= 61 ) and ( age < 110 ):
    print('Пенсионер')
else:
    print('Столько не живут')