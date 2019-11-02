from flask import Flask, render_template

app = Flask(__name__)

# 以下扩展用于在模板中执行do语句
app.jinja_env.add_extension('jinja2.ext.do')

# 循环中使用break continue 需要以下扩展
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if name == 'world':
        name = '<em>World</em>'
    return render_template('hello-1.html', name=name, digits=[1, 2, 3, 4, 5],
                           users=[{'name': 'John'},
                                  {'name': 'Tom', 'hidden': True},
                                  {'name': 'Lisa'},
                                  {'name': 'Tom', 'hidden': True},
                                  {'name': 'Lisa'},
                                  {'name': 'Tom', 'hidden': True},
                                  {'name': 'Lisa'},
                                  {'name': 'Tom', 'hidden': True},
                                  {'name': 'Lisa'},
                                  {'name': 'Bob'}])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
