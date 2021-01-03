import random


WHATS_YOUR_NUMBER = 'What is your number?'
human_wins = 0
robot_wins = 0
draws = 0
while True:
    print(WHATS_YOUR_NUMBER)
    human_number = input()
    if human_number == 'exit game':
        print(f'You won: {human_wins},')
        print(f'The robot won: {robot_wins},')
        print(f'Draws: {draws}.')
        break
    elif not human_number.isdigit() and human_number[0] != '-':
        print('A string is not a valid input!')
    else:
        human_number = int(human_number)
        if human_number < 0:
            print("The number can't be negative!")
        elif human_number > 1_000_000:
            print("Invalid input! The number can't be bigger than 1000000.")
        else:
            goal_number = random.randint(0, 1_000_000)
            robot_number = random.randint(0, 1_000_000)
            print(f'The robot entered the number {robot_number}.')
            print(f'The goal number is {goal_number}.')
            goal_human_difference = abs(goal_number - human_number)
            goal_robot_difference = abs(goal_number - robot_number)
            if goal_human_difference < goal_robot_difference:
                print('You won!')
                human_wins += 1
            elif goal_robot_difference < goal_human_difference:
                print('The robot won!')
                robot_wins += 1
            else:
                print("It's a draw!")
                draws += 1
