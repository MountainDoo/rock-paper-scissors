'''**************************************
Simple Rock, Paper Scissors game         
that ends when the player has 3 victories
**************************************'''
import random

def computer_choice():
    comp_input = random.randint(1, 3)
    if comp_input == 1:
        comp_choice = 'r'
    elif comp_input == 2:
        comp_choice = 'p'
    else:
        comp_choice = 's'
    return comp_choice


def start_game():
    player_score = 0
    computer_score = 0
    games_draw = 0
    total_games = 0
    round_num = 0
    three_wins = 0

    def highest_score():
        if computer_score > player_score:
            high_score = computer_score
        else:
            high_score = player_score
        return high_score

    while three_wins < 3:
        round_num = round_num + 1
        total_games = total_games + 1
        computer = computer_choice()
        player = input('Round ' + str(round_num) + ') Select R, P or S: ').lower()

        if player == 'r' and computer == 'r':
            print('Player chose ' + player.upper())
            print('Computer chose ' + computer.upper())
            print('Draw')
            games_draw = games_draw + 1
        elif player == 'r' and computer == 'p':
            print('Player chose ' + player.upper())
            print('Computer chose ' + computer.upper())
            print('Computer wins')
            computer_score = computer_score + 1
        elif player == 'r' and computer == 's':
            print('Player chose ' + player.upper())
            print('Computer chose ' + computer.upper())
            print('Player wins')
            player_score = player_score + 1
        elif player == 'p' and computer == 'r':
            print('Player chose ' + player.upper())
            print('Computer chose ' + computer.upper())
            print('Player wins')
            player_score = player_score + 1
        elif player == 'p' and computer == 'p':
            print('Player chose ' + player.upper())
            print('Computer chose ' + computer.upper())
            print('Draw')
            games_draw = games_draw + 1
        elif player == 'p' and computer == 's':
            print('Player chose ' + player.upper())
            print('Computer chose ' + computer.upper())
            print('Computer wins')
            computer_score = computer_score + 1
        elif player == 's' and computer == 'r':
            print('Player chose ' + player.upper())
            print('Computer chose ' + computer.upper())
            print('Computer wins')
            computer_score = computer_score + 1
        elif player == 's' and computer == 'p':
            print('Player chose ' + player.upper())
            print('Computer chose ' + computer.upper())
            print('Player wins')
            player_score = player_score + 1
        elif player == 's' and computer == 's':
            print('Player chose ' + player.upper())
            print('Computer chose ' + computer.upper())
            print('Draw')
            games_draw = games_draw + 1
        else:
            print('Game is invalid')

        three_wins = highest_score()
        if player_score > computer_score:
            winner = 'Player 1'
        else:
            winner = 'Computer'

    print('\nRESULTS\n----------------')
    print('Total games played: ' + str(total_games))
    print('Total draw games: ' + str(games_draw))
    print('Player score: ' + str(player_score))
    print('Computer score: ' + str(computer_score))
    print('The winner is ' + winner + '!')


start_game()
