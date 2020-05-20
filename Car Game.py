started = False
while True:
    command = input().lower()
    if command == 'start':
        if started:
            print('Car has already started')
        else:
            started = True
            print("Vroom...vroom! Car is ready. Let's go!")
    elif command == 'stop':
        if not started:
            print('Car has already stopped')
        else:
            started = False
            print("Car has stopped")
    elif command == 'help':
        print(''' 
start - to start the car
stop - to stop the car /n
quit - to exit the game 
    ''')
    elif command == 'quit'.lower():
        print('Good Bye!')
        break
    else:
        print("I don't understand that")




