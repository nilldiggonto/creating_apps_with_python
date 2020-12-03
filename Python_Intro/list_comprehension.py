
digit_list = [x for x in range(10)]
print(digit_list)
print(type(digit_list))

multiply_list = [x**2 for x in range(5)]
print(multiply_list)

## Creating all even numbers
even_number = [x for x in range(20) if x%2==0]
print(even_number)

##
game_upper = ['HADES', 'LIMBO', 'COMMET','CRISYS']

game_lower = [game.strip().lower() for game in game_upper ]
print(game_lower)

#################
def your_friends():
    friend = input('Type your friends name separated by comma: \n')
    

    friend_without_space= [ f.strip() for f in friend.split(',')]
   
    return friend_without_space

def your_best_friend():
    best_friend = input('Type your Best Friends name: \n')
    if best_friend in your_friends():
        print (f'{best_friend} is your best friend')
    else:
        print(f'{best_friend} is not even in your friend list')

your_best_friend()