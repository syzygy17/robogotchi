import random


WHATS_YOUR_NUMBER = 'What is your number?'
WHICH_GAME = 'Which game would you like to play?'
WHATS_YOUR_MOVE = 'What is your move?'
NUMBERS_GAME = 'Numbers'
ROCK_PAPER_SCISSORS_GAME = 'Rock-paper-scissors'
battery = 100
overheat = 0
skills = 0
boredom = 0
rps_list = ['rock', 'scissors', 'paper']


print('How will you call your robot?')
robot_name = input()

while True:
    print()
    print(f'Available interactions with {robot_name}:')
    print('exit – Exit')
    print('info – Check the vitals')
    print('recharge – Recharge')
    print('sleep – Sleep mode')
    print('play – Play')
    print('Choose:')
    if overheat >= 100:
        print(f'The level of overheat reached 100, {robot_name} has blown up! Game over. Try again?')
        break
    chosen = input()
    if chosen == 'exit':
        print('Game over')
        break
    elif chosen == 'info':
        print(f'{robot_name}\'s stats are: battery is {battery},')
        print(f'overheat is {overheat},')
        print(f'skill level is {skills},')
        print(f'boredom is {boredom}.')
    elif chosen == 'recharge':
        if battery == 100:
            print(f'{robot_name} is charged!')
        else:
            print(f'{robot_name}\'s level of overheat was {overheat}.', end=' ')
            if overheat - 5 <= 0:
                overheat = 0
            else:
                overheat -= 5
            print(f'Now it is {overheat}.')
            print(f'{robot_name}\'s level of the battery was {battery}. Now it is {battery + 10}.')
            battery += 10
            print(f'{robot_name}\'s level of boredom was {boredom}. Now it is {boredom + 5}.')
            boredom += 5
            print(f'{robot_name} is recharged!')
    elif chosen == 'sleep':
        if overheat == 0 and overheat - 20 <= 0:
            print(f'{robot_name} is cool!')
        else:
            insertion = ''
            if overheat - 20 > 0:
                insertion = f'{robot_name} cooled off!'
            else:
                insertion = f'{robot_name} is cool!'
            print(f'{robot_name}\'s level of overheat was {overheat}.', end=' ')
            if overheat - 20 <= 0:
                overheat = 0
            else:
                overheat -= 20
            print(f'Now it is {overheat}.')
            print(insertion)
    elif chosen == 'play':
        human_wins = 0
        robot_wins = 0
        draws = 0
        print(WHICH_GAME)
        game = input()
        play_or_not = True
        while play_or_not:
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
                game = input()
        if not play_or_not:
            print(f'{robot_name}\'s level of boredom was {boredom}.', end=' ')
            if boredom - 10 <= 0:
                boredom = 0
            else:
                boredom -= 10
            print(f'Now it is {boredom}.')
            print(f'{robot_name}\'s level of overheat was {overheat}. Now it is {overheat + 10}.')
            overheat += 10
    else:
        print('Invalid input, try again!')
