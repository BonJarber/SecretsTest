#!/usr/bin/python
# coding: utf-8
from flask import Flask
import config

app = Flask(__name__)

@app.route('/1')
def one():
    # hardcoded api secret
    headers = {'X-API-KEY' : 'CkSaSTFTEJ4BSpSAULQJBvpc586JhCxT'}

@app.route('/')
def entry_point():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)