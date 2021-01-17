from flask import Flask, render_template, request
from googletrans import Translator


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/lang',methods = ['POST'])
def login():
    message = request.form['message']
    language = request.form['language']
    translator = Translator()
    output = translator.translate(message, dest=language).text
    
    return render_template("home.html", output_message=output)


if __name__=='__main__':
    app.run()
