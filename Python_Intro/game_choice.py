####### A simple user game . To check if someone know the game or not
def which_game_you_like(games):
    known = []
    for game in games:
        known.append(game)
    return known

admin = True
games = []
while admin:
    
    user_input = input('Type a name: ')
    games.append(user_input)
    user_ask = input('Do you want to add more? (y/n)')
    if user_ask == 'n':
        admin = False

print(which_game_you_like(games)) 



def user_answer(game):
    if game in games:
        print('ow nice you know the game')
    else:
        print('okay, you belong to other community')

new_user = input('Name a game you like: ')
user_answer(new_user)
    