#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""json_server"""
# @Time    : 2019/10/21 16:19
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
from flask import Flask, request, jsonify

app = Flask(__name__)


# 处理客户端client传来的json串
@app.route('/')
def index():
    print(type(request.json))
    print(request.json)
    result = request.json['value1'] + request.json['value2']
    return str(result)

# 将服务器的json串返回给客户端client2
@app.route('/res_json')
def index2():
    result = {'key1': 'value1', 'key2': 'value2'}
    # return Response(json.dumps(result), mimetype='application/json')
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, processes=True)
