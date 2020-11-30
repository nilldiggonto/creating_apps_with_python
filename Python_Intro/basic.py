#Variable 
five = 5
six = 6
print(five* six)

#String Variable
person_one = 'I said the number: '
person_two = 'I have different number: '
print(person_one,five)
print(person_two,six)
print('Sum of their Number: ', five*six)
print(print(5)) #will print None

## creating custom Method
def print_something():
    print('Who is there?')
    
print_something() #calling method

## Using parameter
def print_new(my_params):
    print('What is the number: ',my_params)

print_new(five*six)
print_new(six)

## Using multiple Parameter
def print_multi(one,two):
    return one*two

result = print_multi(five,six)
print('So, the new result is', result)

#nested method
print_new(print_multi(five,six))