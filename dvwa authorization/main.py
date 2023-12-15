from datetime import time
from flask import Flask, render_template, request

app = Flask(__name__)

login = "test"
password = "qwerty"
start = 0

@app.route('/')
def log():
    return render_template('design.html')

@app.route('/log', methods=['GET', 'POST'])
def login_user():
    global start

    if request.method == 'GET':
        return render_template('log.html')

    login_input = request.form.get('login', 'defaultLogin')
    password_input = request.form.get('password', 'defaultPassword')

    if login_input == 'defaultLogin':
        return render_template('log.html')

    if start > int(time.time() * 1000):
        message = "Подождите {} минут. Прежде чем пробовать снова".format(
            (start - int(time.time() * 1000)) // (1000 * 60)
        )
        return render_template('log.html', message=message)

    condition = False
    if login_input == login and password_input == password:
        condition = True

    if condition:
        message = "С возвращением {}!".format(login_input)
    else:
        start = int(time.time() * 1000) + 1000 * 60 * 15
        message = "Логин или пароль введены неверно!"

    return render_template('log.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
