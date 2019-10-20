print('Welcome, player1 and player2 to the game...\n ROCK, PAPER, SCISSORS, SHOOT!')
print('The options are: rock, paper and scissors.')
enter = 'y'
while enter == 'y':
    print('ROCK, PAPER, SCISSORS, SHOOT!')
    player1 = input('player1, what did you do?\n')
    player2 = input('player2, what did you do?\n')
    if player1 == player2:
        print("It's a draw!")
    elif player1 == 'rock':
        if player2 == 'scissors':
            print('player1 won!')
        else:
            print('player2 won!')
    elif player1 == 'paper':
        if player2 == 'scissors':
            print('player2 won!')
        else:
            print('player1 won!')
    elif player1 == 'scissors':
        if player2 == 'rock':
            print('player2 won!')
        else:
            print('player1 won!')
    else:
        print('One of the answers is incorrect.')
    enter = input('Do you want to continue? (y/n)\n')
print('Bye!')