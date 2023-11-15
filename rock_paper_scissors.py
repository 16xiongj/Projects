import random

user_wins = 0
computer_wins = 0
draws = 0

options = ["rock", "paper", "scissor"]

while True:
    computer = options[random.randint(0,3)]
    print('Welcome to rock, paper, scissors!')
    user_input = input("Choose! rock/paper/scissors or 'Q' to quit:  ").lower()
    
    if user_input == 'q':
        break
    
    elif user_input not in options:
        print('Invalid response.')
        continue

    elif user_input == computer:
        print('DRAW')
        draws += 1

    elif user_input == 'rock' and computer == 'scissor':
        print('You WIN!')
        user_wins += 1

    elif user_input == 'Paper' and computer == 'rock':
        print('You WIN!')
        user_wins += 1

    elif user_input == 'scissor' and computer == 'paper':
        print('You WIN!')
        user_wins += 1

    else:
        print('You Lost')
        computer_wins += 1

print('You won ' + str(user_wins))
print('Computer won ' + str(computer_wins))
print('Total Draws: ' + str(computer_wins))