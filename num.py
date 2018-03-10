from flask import Flask, render_template, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def home():
    if not session.get('guessit'):
        session['guessit'] = 0
    elif session['guessit'] = 0:
        session['guessit'] = random.randrange(1, 101)
    session['display_result'] = "<div></div>"
    return render_template('index.html', result_of_guess = session['display_result'])

@app.route('/check', methods=['POST'])
def check():
    if guess == session['guessit']:
        # display correct anwser
        return redirect('/showgot')
        
    elif guess > session['guessit']:
        # desplay Too High!
        return redirect('/showhigh')
        session['display_result'] = "<div></div>"
    else:
        # display Too Low!
        return redirect('/showlow')

@app.route('/showlow')
def show_low():
  return render_template('low.html')    

@app.route('/showhigh')
def show_high():
  return render_template('high.html')

@app.route('/showgot')
def show_got():
  return render_template('got.html')

@app.route('/reset')
def reset():
    # reset the random number and redirect to the home page
    session['guessit'] = 0 
    return redirect('/')

app.run(debug=True)