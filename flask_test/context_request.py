#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""context_request"""
# @Time    : 2019/10/24 15:07
# @Author  : Wind
# @Des     : 上下文
# @Software: PyCharm
from flask import Flask, g, request, template_rendered, render_template, request_started, request_finished, \
    request_tearing_down, got_request_exception, appcontext_tearing_down, appcontext_pushed, appcontext_popped, \
    message_flashed

app = Flask(__name__)


@app.before_request
def before_request():
    print('before request started')
    print(request.url)


@app.before_request
def before_request2():
    print('before request started 2')
    print(request.url)
    g.name = "SampleApp"


@app.after_request
def after_request(response):
    print('after request finished')
    print(request.url)
    response.headers['key'] = 'value'
    return response


@app.teardown_request
def teardown_request(exception):
    print('teardown request')
    print(request.url)


@app.teardown_appcontext
def teardown_app(exception):
    print('teardown application')


@app.route('/')
def index():
    # eturn 'Hello, %s!' % g.name
    return render_template('hello.html')


# Capture flask core signals #
@template_rendered.connect_via(app)
def with_template_rendered(sender, template, context, **extra):
    print('Using template: %s with context: %s' % (template.name, context))
    print(request.url)


@request_started.connect_via(app)
def print_request_started(sender, **extra):
    print('Signal: request_started')


@request_finished.connect_via(app)
def print_request_finished(sender, response, **extra):
    print('Signal: request_finished')


@got_request_exception.connect_via(app)
def tmp(sender, exception, **extra):
    print('exception')


@request_tearing_down.connect_via(app)
def print_request_tearingdown(sender, exc, **extra):
    print('Signal: request_tearing_down')


@appcontext_tearing_down.connect_via(app)
def tmp(sender, **extra):
    print('app_context_tear_down')


@appcontext_pushed.connect_via(app)
def tmp(sender, **extra):
    print('push_app_ctx_stack')


@appcontext_popped.connect_via(app)
def tmp(sender, **extra):
    print('pop_app_ctx_stack')


@message_flashed.connect_via(app)
def tmp(sender, message, category, **extra):
    print('message')

# Request Context Hook #
@app.before_request
def before_request():
    print('Hook: before_request')


@app.after_request
def after_request(response):
    print('Hook: after_request')
    return response


@app.teardown_request
def teardown_request(exception):
    print('Hook: teardown_request')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
