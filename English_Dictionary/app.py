import json
from difflib import get_close_matches
data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) >0:
        check= input('Did you mean %s?\n Enter Y is for Yes \n Enter N for No\n' % get_close_matches(word,data.keys())[0])
        if check.lower() == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif check.lower() == 'n':
            return 'We dont know what you want'
        else:
            return 'sorry try again'


    else:
        return 'The Word dont exist'

word = input('Enter a word: ')

output = translate(word)

if type(output) == list:
    for w in output:
        print(w)
else:
    print(output)