
import requests
# the website that game happens
res = requests.get('https://www.nytimes.com/').text
# choose the number of players
num_players = int(input('How many players: '))
score_players = {}
# choose player name
for i in range(num_players):
    player_name = input(f'Player {i + 1} Name: ')
    score_players[player_name] = 0
continue_game = True
max_score = 5
while continue_game:
    # select a word for search in website
    for player_name in score_players.keys():
        user_input = input(f'{player_name}s word: ')
        # condition if the player gets a +1 to score
        if user_input in res:
            score_players[player_name] += 1
            print('Success')
            print(score_players)
        else:
            print('Fail')
            print(score_players)
    winners = []

    # check amount of winners
    for player_name, player_score in score_players.items():
        if player_score == max_score:
            winners.append(player_name)
            # print(f'{player_name} Win!')
            continue_game = False
    # at the end of the game showing up a winner
    if len(winners) == 1:
        print(f'{winners[0]} Win!')
    elif len(winners) > 1:
        print('Tie')
        print('Winners: ')
        for winner in winners:
            print(winner)




