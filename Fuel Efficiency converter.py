eff = float(input("Please compute your car's fuel efficiency "))
unit = input("Please select 'L' if the unit is in L/100km or 'M' if the unit is in MPG ")

if unit.upper() == 'L':
    converted = round((235.215/eff),2)
    print(f"Your car's fuel efficiency equivalent to American units is " + f'{converted} MPG')
elif unit.upper() == 'M':
    converted = round((235.215/eff),2)
    print(f"Your car's fuel efficiency equivalent to Canadian units is " + f'{converted} L/100km')
else:
    print("Please only select either 'L' or 'M'")
