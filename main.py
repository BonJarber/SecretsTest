#!/usr/bin/python
# coding: utf-8
from flask import Flask
import config
import requests
import psycopg2
import redis

app = Flask(__name__)

@app.route('/req_1')
def req_one():
    # hardcoded api secret in obvious header
    headers = {'X-API-KEY' : 'CkSaSTFTEJ4BSpSAULQJBvpc586JhCxT'}
    results = requests.get('https://bonjarber.com/', headers=headers)
    return results.text

@app.route('/req_2')
def req_two():
    # hardcoded secret in request
    results = requests.get('https://bonjarber.com/', auth=('admin','password'))
    return results.text

@app.route('/req_3')
def req_three():
    # config secret in obvious header
    headers = {'X-API-KEY' : config.SOURCE_7}
    results = requests.get('https://bonjarber.com/', headers=headers)
    return results.text

@app.route('/req_4')
def req_four():
    # config secret in request
    results = requests.get('https://bonjarber.com/', auth=('admin', config.SOURCE_1))
    return results.text

@app.route('/req_5')
def req_five():
    # config secret in obscure header
    headers = {'X-CUSTOM-HEADER' : config.SOURCE_6}
    results = requests.get('https://bonjarber.com/', headers=headers)
    return results.text

@app.route('/req_6')
def req_six():
    # hardcoded secret in obscure header
    headers = {'X-CUSTOM-HEADER' : 'r87hh5MgYZwYWqk7yzmvvG'}
    results = requests.get('https://bonjarber.com/', headers=headers)
    return results.text

@app.route('/req_7')
def req_seven():
    # hardcoded secret in obvious post body
    data = {'password' : 'r87hh5MgYZwYWqk7yzmvvG'}
    results = requests.get('https://bonjarber.com/', data=data)
    return results.text

@app.route('/req_8')
def req_eight():
    # config secret in obvious post body
    data = {'password' : config.SOURCE_4}
    results = requests.get('https://bonjarber.com/', data=data)
    return results.text

@app.route('/req_9')
def req_nine():
    # hardcoded secret in obscure post body
    data = {'value' : 'r87hh5MgYZwYWqk7yzmvvG'}
    results = requests.get('https://bonjarber.com/', data=data)
    return results.text

@app.route('/req_10')
def req_ten():
    # config secret in obscure post body
    data = {'value' : config.SOURCE_5}
    results = requests.get('https://bonjarber.com/', data=data)
    return results.text

@app.route('/pos_1')
def pos_one():
    # config secret in postgres connection
    conn = psycopg2.connect(
        host="localhost",
        database="test",
        user="postgres",
        password=config.SOURCE_3)
    return conn

@app.route('/pos_2')
def pos_2():
    # config secret in postgres connection
    conn = psycopg2.connect(
        host="localhost",
        database="test",
        user="postgres",
        password="vsecret")
    return conn

@app.route('/red_1')
def red_one():
    # config secret in redis connection
    redis_db = redis.StrictRedis(host="localhost", port=6379, db=0, password=config.SOURCE_2)
    return redis_db

@app.route('/red_2')
def red_2():
    # hardcoded secret in redis connection
    redis_db = redis.StrictRedis(host="localhost", port=6379, db=0, password='redis')
    return redis_db

@app.route('/')
def entry_point():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)