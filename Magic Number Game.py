secret_number = 7
guess_count = 0
guess_limit = 3

while guess_count < guess_limit: #While function acts as a 'loop' until condition fulfilled
    guess = int(input('Guess my magic Number (0-9): '))
    guess_count += 1
    if guess == secret_number:
        print("You Won!")
        break #break function provide exit for the function, when the condition fulfilled
else:
    print('Sorry..you have lost!')





