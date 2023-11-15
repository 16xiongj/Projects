import random

#///////
#  Asks for input from user for the highest number and checks if the input is valid.
#///////
top_of_range = input('Type a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please enter a number larger than 0. ')
        quit()

else:
    print('Please type a number.')
    quit()


#///////
#  Generates the target number.
#///////
random_number = random.randint(0, top_of_range)


#///////
#  User plays the game making a guess and its being compared to the Target number.
#///////
num_of_guesses = 0

while True:
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if top_of_range <= 0:
            print('Please enter a number larger than 0. ')
            quit()
    else:
        print('Please type a number.')
        continue

    if user_guess == random_number:
        print('You got it correct!')
        print('It took you: ' + str(num_of_guesses))
        break()
    else:
        print('You got it wrong!')
        num_of_guesses += 1
    
def play_again():
    pass