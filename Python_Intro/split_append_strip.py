def your_friends():
    friend = input('Type your friends name separated by comma: \n')
    friend_list = friend.split(',')

    friend_without_space= []
    for f in friend_list:
        friend_without_space.append(f.strip())
    return friend_without_space

def your_best_friend():
    best_friend = input('Type your Best Friends name: \n')
    if best_friend in your_friends():
        print (f'{best_friend} is your best friend')
    else:
        print(f'{best_friend} is not even in your friend list')

your_best_friend()
