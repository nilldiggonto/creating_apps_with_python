word = 'There are some words'

for letter in word:
    print(letter)


list = [1,2,3,4,5,6]
for l in list:
    print(l*2)

admin = True
while admin == True:
    user_id = '#$@$%@'
    print(user_id)

    user_input = input('want to exit?(y/n)')
    if user_input == 'y':
        admin = False


def item(a,b):
    if a == b:
        for i in range(a):
            print(b)

item(5,5)   


game = ['hades','limbo','inside','Gta']
print(game)
game_name = input('Name a game you played before? \n')


if game_name in game:
    print(f'{game_name} ! i have played')
else:
    print(f'{game_name}! i have played')


#EVEN NUMBER
numbers = [1,2,3,4,5,6,7,8,9,10]
def even_number(numbers):
    even =[]
    for number in numbers:
        if number % 2 ==0:
            even.append(number)

    return even

print(even_number(numbers))

# creating user choice
def user_choice(choice):
    if choice == 'a':
        return 'add'
    else:
        return 'quit'

user_input = input('To add type (a) to quit type (q)' )
print(user_choice(user_input))


