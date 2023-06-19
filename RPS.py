import random

user_wins = 0
cpu_wins = 0
draws = 0

options = ['rock', 'paper', 'scissors']

rock = 0
paper = 0
scissors = 0

usage = [rock, paper, scissors]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break
        #print('Goodbye!')
        #quit()

    if user_input not in options:
        print('This is not a valid input, please try again.')
        continue
    
    if user_input == 'rock':
        usage[0] += 1
    if user_input == 'paper':
        usage[1] += 1
    if user_input == 'scissors':
        usage[2] += 1

    most_used = usage.index(max(usage))

    random_number = random.randint(0, 2)
    # 0 = Rock, 1 = Paper, 2 = Scissors
    computer_choice = options[random_number]
    print("Computer Choice:", computer_choice.title() + ".")

    if user_input == computer_choice:
        print("It's a Draw.")
        draws += 1
        
    elif user_input == 'rock' and computer_choice == 'scissors':
        print('You Win!')
        user_wins += 1
    
    elif user_input == 'paper' and computer_choice == 'rock':
        print('You Win!')
        user_wins += 1
    
    elif user_input == 'scissors' and computer_choice == 'paper':
        print('You Win!')
        user_wins += 1
    
    else:
        print("You Lose!")
        cpu_wins += 1
        
print("----------------------------------")
print("You played " + str(user_wins + cpu_wins + draws) + " games.") 
print("You won " + str(user_wins) + " times.")
print("The Computer won " + str(cpu_wins) + " times.")
print("There were " + str(draws) + " draws.")
print("Your most played was " + options[most_used].title() + " you played it " + str(max(usage)) + " times.")
print('Goodbye!')
print("----------------------------------")
