from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '34d7823c19b2e8ff040e750cd571fd71'


@app.route('/')
def start_page():
    return render_template('start.html')


@app.route('/register', mrthods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route('/contact')
def contact_page():
    return render_template('contact.html', title='Contact')


@app.route('/DAX')
def dax_chart():
    return render_template('dax.html', title='DAX')


@app.route('/NDX')
def ndx_chart():
    return render_template('ndx.html', title='NDX')


@app.route('/SPX')
def spx_chart():
    return render_template('spx.html', title='SPX')


@app.route('/USDAUD')
def us_chart():
    return render_template('usdaud.html', title='USD/AUD')


@app.route('/WIG20')
def wig_chart():
    return render_template('wig.html', title='WIG20')


if __name__ == "__main__":
    app.run(debug=True)
