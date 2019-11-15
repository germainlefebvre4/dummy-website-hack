import os
import datetime

from flask import Flask, render_template, request
app = Flask(__name__)

login_username='jean'
login_password='jean'

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/login')
def login():
    print(request.args)
    if 'username' in request.args.keys():
        if request.args['username'] == login_username:
            username = request.args.get('username')
            if 'password' in request.args.keys():
                if request.args['password'] == login_password:
                    return render_template('login-success.html', username=login_username)
                else:
                    return render_template('login-error.html', error="password")
            else:
                return render_template('login-parameters.html', param="password")
        else:
            return render_template('login-error.html', error="username")
    else:
        return render_template('login-parameters.html', param="username")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

