from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '34d7823c19b2e8ff040e750cd571fd71'


@app.route('/')
def start_page():
    return render_template('start.html')


@app.route('/register')
def registration():
    registration_form = RegistrationForm()
    return render_template('register.html', title='Register', form=registration_form)


@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', title='Login', form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
