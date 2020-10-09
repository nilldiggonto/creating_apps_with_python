from flask import Flask,render_template,request
import json
from difflib import get_close_matches


data = json.load(open('data.json'))

app = Flask(__name__)

############################

@app.route('/',methods=["GET","POST"])
def index():
    check = ""
    word_type = ""
    word = ""
    word_p = ""

    
    if request.method == 'POST':
        word_p = request.form.get('word')
        word = word_p.lower()
        

        if word in data:
            word = data[word]
            word_type = type(word)

        elif len(get_close_matches(word,data.keys()))>0 :
            check = get_close_matches(word,data.keys())[0]


        else:
            word = "The word doesn't exist!"


    return render_template('main.html',word=word,check=check,word_type=word_type,word_p=word_p)



############################
if __name__ == "__main__":
    app.run(debug=True)