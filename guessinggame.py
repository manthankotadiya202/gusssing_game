from random import randint


def guessing_game():
    rand_num = randint(1, 100)  # we are generating a random int b/w 1, 100
    counter = 0
    while True:
        guess_num = int(input('Guess a number b/w 1 to 100:'))
        counter += 1
        if rand_num > guess_num:
            print('Guess something bigger!')
        elif rand_num < guess_num:
            print('Guess something smaller')
        else:
            print(f'the game is over , and it took you {counter} time to guess it')
            break
    return counter


def play_separately():
    print('PLAYER PLAY GAME SEPARATELY')
    player1 = input('Enter player 1 name:')
    counter1 = guessing_game()
    print(f'Player1: {player1}\nScore: {counter1}', end="\n\n")

    player2 = input("Enter player 2 name:")
    counter2 = guessing_game()
    print(f'Player2: {player2}\nScore: {counter2}', end="\n\n")
    return player1, counter1, player2, counter2


def evaluate_score(player1_score, p1_name, player2_score, p2_name, last_guess=None):
    if not last_guess:
        if player1_score == player2_score:
            print("The game is a tie!")
            return

        if player1_score > player2_score:
            print(f"Player 2: {p2_name} won the game!")
        else:
            print(f"Player 1: {p1_name} won the game!")
    else:
        if last_guess % 2 == 0:
            print(f'Player 1 {p1_name} won the game!')
        else:
            print(f'Player 2 {p2_name} won the game!')


def guessing_game_together(player1, player2):
    rand_num = randint(1, 100)  # we generating a random int 1, 100
    counter1 = 0
    counter2 = 0
    turn = randint(0, 1)
    while True:
        if turn % 2 == 0:
            print(f'{player1} its your turn to guess:')
        else:
            print(f'{player2} its your turn to guess:')
        guess_num = int(input('Guess a number b/w 1 to 100:'))
        if turn % 2 == 0:
            counter1 += 1
        else:
            counter2 += 1
        if rand_num > guess_num:
            print('Guess something bigger!')
        elif rand_num < guess_num:
            print('Guess something smaller')
        else:
            print(f'Game is over!')
            break
        turn += 1
    return counter1, counter2, turn


def play_together():
    print('PLAYER PLAY GAME TOGETHER')
    player1 = input('Enter player 1 name:')
    player2 = input('Enter player 2 name:')
    list_1 = [player1, player2]
    counter1, counter2, turn = guessing_game_together(player1, player2)
    evaluate_score(counter1, player1, counter2, player2, turn)


if __name__ == '__main__':
    player1_name, result1, player2_name, result2 = play_separately()
    evaluate_score(result1, player1_name, result2, player2_name)
    play_together()
