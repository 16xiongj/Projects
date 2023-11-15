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
num_of_guesses = 1

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
        print('It took you: ' + str(num_of_guesses) + ' try!')
        break
    else:
        # ADD a case where it tells you if you are lower or higher
        print('You got it wrong!')
        if user_guess < random_number:
            print('The number is higher')
        else:
            print('The number is lower')
        num_of_guesses += 1

#
#  Gives the option to play again and resets the game.
#  **Add the play again option
#

# def play_again():
#     while True:
#         user_answer = input('Do you want to play again?(Y/N) ').upper()

#         if user_answer.isalpha():
#             if user_answer == 'Y':
#                 main()                                # will need to make the main program a def
#             else if user_answer == 'N':
#                 print('Thanks for playing!')
#                 break()
#             else:
#                 print()
                


