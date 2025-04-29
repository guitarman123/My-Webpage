import random

choices = ('r', 'p', 's')


while True:
    user_input = input('Rock, Paper, or Scissors? (r/p/s): ').lower()


#player's choice
    if user_input == 'r':
        print('You chose 🧱')
    elif user_input == 'p':
        print('You chose 📄')
    elif user_input == 's':
        print('You chose ✂')
    elif user_input not in choices:
            print('Invalid choice')
            continue

#computer's choice
    computers_rps = ['🧱', '📄', '✂']
    computer_choice = random.choice(computers_rps)
    print(f'Computer chose {computer_choice}')


#see if player or computer won

#handles ties
    if user_input == 'r' and computer_choice == '🧱':
        print('Tie!')
    if user_input == 'p' and computer_choice == '📄':
        print('Tie!')
    if user_input == 's' and computer_choice == '✂':
        print('Tie!')

#handles player wins
    if user_input == 'r' and computer_choice == '✂':
        print('You win!')
    if user_input == 'p' and computer_choice == '🧱':
        print('You win!')
    if user_input == 's' and computer_choice == '📄':
        print('You win!')

#handles computer wins
    if user_input == 'r' and computer_choice == '📄':
        print('You lose!')
    if user_input == 'p' and computer_choice == '✂':
        print('You lose!')
    if user_input == 's' and computer_choice == '🧱':
        print('You lose!')

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break

