from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def home():
    if not session.get('guessit'):
        session['guessit'] = 0
        session['guessit'] = random.randrange(1, 101)
        session['display_result'] = "none"
    elif session['guessit'] == 0:
        session['guessit'] = random.randrange(1, 101)
    print session['guessit']
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    if int(request.form['guess']) == session['guessit']:
        # display correct anwser
        session['display_result'] = "correct"
    elif int(request.form['guess']) > session['guessit']:
        # desplay Too High!
        session['display_result'] = "high"
    else:
        # display Too Low!
        session['display_result'] = "low"
    return redirect('/')

@app.route('/reset')
def reset():
    # reset the random number and redirect to the home page
    session['display_result'] = "none"
    session['guessit'] = 0 
    return redirect('/')

app.run(debug=True)