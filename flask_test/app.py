# -*- encoding = UTF-8
"""flask测试"""
from flask import Flask
from flask import Flask
from flask import request, url_for

app = Flask(__name__, static_folder='files')


@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        name = 'World'
    return 'Hello %s' % name


@app.route('/user/<int:user_id>')
def get_user(user_id):
    return 'User ID: %d' % user_id


@app.route('/login', methods=['get', 'POST'])
def login():
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'


@app.route('/path')
def path():
    # return url_for('login')
    # return url_for('login', id='1')
    # return url_for('hello', name='man')
    return url_for('static', filename='style.css')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
