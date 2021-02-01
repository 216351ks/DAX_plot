from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def start_page():
    return render_template('start.html')

@app.route('/login')
def user_login():
    return render_template('login.html', title = 'Login')

@app.route('/contact')
def contac_page():
    return render_template('contact.html', title = 'Contact')

if __name__ == "__main__":
    app.run(debug=True)
