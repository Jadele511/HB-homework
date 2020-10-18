from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    if session['name']: 
        return render_template('form.html')
    else:
        return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    return render_template('/form.html')

@app.route('/results')
def show_results():
    message = request.args.get('message')
    if message == 'cheery':
        message = 'You look super gorgoeus today!!'
    elif message == 'honest':
        message = 'It is such a lovely day.'
    else:    
        message = 'Covid kills more people than we thought'

    return render_template('results.html', name =session['name'], message=message)

@app.route('/save-name')
def save_name():
    user_name = request.args.get('username')
    session['name'] = user_name    
    return render_template('/form.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
