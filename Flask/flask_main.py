# -*- coding: utf-8 -*-
"""
Flsk: a web based microservice framework which allows our ml_model to share
using the web based API

After the http://127.0.0.1/hello:9000/?a=10&b=30&c=60
@app.route('/hello', methods=['GET', 'POST'])

Note:
    At the times when we have to supply inputs like images and files
    GET does not support uploading multimedia
    then POST is required
"""

from flask import Flask,request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def add():
    """
    a = request.args.get("a")
    b = request.args.get("b")
    c = request.args.get("c")
    """
    a = request.form["a"]
    b = request.form["b"]
    c = request.form["c"]
    return str(int(a)+int(b)+int(c))

if __name__ == '__main__':
    app.run(port=9000)