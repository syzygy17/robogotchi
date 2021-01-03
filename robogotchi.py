import random


WHATS_YOUR_NUMBER = 'What is your number?'
WHICH_GAME = 'Which game would you like to play?'
WHATS_YOUR_MOVE = 'What is your move?'
NUMBERS_GAME = 'Numbers'
ROCK_PAPER_SCISSORS_GAME = 'Rock-paper-scissors'
human_wins = 0
robot_wins = 0
draws = 0
play_or_not = True
rps_list = ['rock', 'scissors', 'paper']

while play_or_not:
    print(WHICH_GAME)
    game = input()
    if game == NUMBERS_GAME:
        while True:
            print(WHATS_YOUR_NUMBER)
            human_number = input()
            if human_number == 'exit game':
                print(f'You won: {human_wins},')
                print(f'The robot won: {robot_wins},')
                print(f'Draws: {draws}.')
                play_or_not = False
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
    elif game == ROCK_PAPER_SCISSORS_GAME:
        while True:
            print(WHATS_YOUR_MOVE)
            human_move = input()
            if human_move == 'exit game':
                print(f'You won: {human_wins},')
                print(f'Robot won: {robot_wins},')
                print(f'Draws: {draws}.')
                play_or_not = False
                break
            elif human_move not in rps_list:
                print('No such option! Try again!')
            else:
                robot_move = random.choice(rps_list)
                print(f'Robot chose {robot_move}')
                if robot_move == human_move:
                    print("It's a draw!")
                    draws += 1
                elif robot_move == rps_list[0] and human_move == rps_list[2]:
                    print('You won!')
                    human_wins += 1
                elif robot_move == rps_list[2] and human_move == rps_list[0]:
                    print('The robot won!')
                    robot_wins += 1
                elif robot_move == rps_list[0] and human_move == rps_list[1]:
                    print('The robot won!')
                    robot_wins += 1
                elif robot_move == rps_list[1] and human_move == rps_list[0]:
                    print('You won!')
                    human_wins += 1
                elif robot_move == rps_list[2] and human_move == rps_list[1]:
                    print('You won!')
                    human_wins += 1
                elif robot_move == rps_list[1] and human_move == rps_list[2]:
                    print('The robot won!')
                    robot_wins += 1
    else:
        print('Please choose a valid option: Numbers or Rock-paper-scissors?')
