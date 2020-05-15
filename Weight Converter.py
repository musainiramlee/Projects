Weight = int(input('Your Weight? '))
unit = input('(L)bs or (K)g ')

if unit.upper() == 'L':
    converted = round((Weight/2.20462),1)
    print(f'Your weight is {converted} kilos')
else:
    converted = round((Weight*2.20462),1)
    print(f'Your weight is {converted} pounds')



