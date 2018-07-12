# The Penalty-kick game

from random import choice

user_score = 0
comp_score = 0

for turn in range(1, 10):
    print(turn, 'PENALTY')

    print('You:', user_score, 'Vintage:', comp_score)

    user_player = input('Pick a spot!|L, C, R|: ')

    comp_gk = choice(['L', 'C', 'R'])
    print(comp_gk)

    comp_player = choice(['L', 'C', 'R'])

    user_goalie = input('Save your goal!|L, C, R|: ')

    if user_player != 'L' and user_player != 'C' and user_player != 'R':
        print('Ooh! you missed the target!')

    if user_player == 'L' or user_player == 'C' or user_player == 'R':
        if user_player == comp_gk:
            print('Saved! Brilliant goalkeeping!!')
        elif user_player != comp_gk:
            print('Goal! Goal!!')
            user_score += 1

    if comp_player == 'L' or comp_player == 'C' or comp_player == 'R':
        if comp_player == user_goalie:
            print('Saved! Electric Stuff!!')
        elif comp_player != user_goalie:
            print('Get in!!')
            comp_score += 1

    if turn == 5:
        if user_score > comp_score or user_score < comp_score:
            if user_score > comp_score:
                print('You win!')
            elif user_score < comp_score:
                print('Vintage downs Human!')
            print("It's over here")
            print('You:', user_score, 'Vintage:', comp_score)
            break
    elif turn > 5:
        if user_score > comp_score or user_score < comp_score:
            if user_score > comp_score:
                print('Computer well dispatched.You win!')
            elif user_score < comp_score:
                print('Vintage downs Human!')
            print("It's over here")
            print('You:', user_score, 'Vintage:', comp_score)
            break
