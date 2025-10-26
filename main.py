#!/usr/bin/python
# coding: utf-8
from flask import Flask
import config
import requests
import psycopg2
import redis
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', os.urandom(24).hex())

@app.route('/req_1')
def req_one():
    # Use environment variable for API secret
    api_key = os.getenv('API_KEY_REQ_1', config.API_KEY)
    if not api_key:
        return "API key not configured", 500
    headers = {'X-API-KEY': api_key}
    results = requests.get('https://bonjarber.com/', headers=headers)
    return results.text

@app.route('/req_2')
def req_two():
    # Use environment variables for authentication
    username = os.getenv('API_USERNAME', 'admin')
    password = os.getenv('PASSWORD', config.PASSWORD)
    if not password:
        return "Authentication not configured", 500
    results = requests.get('https://bonjarber.com/', auth=(username, password))
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
    # Use environment variable for custom header
    custom_header_value = os.getenv('CUSTOM_HEADER_VALUE', config.SOURCE_6)
    if not custom_header_value:
        return "Custom header value not configured", 500
    headers = {'X-CUSTOM-HEADER': custom_header_value}
    results = requests.get('https://bonjarber.com/', headers=headers)
    return results.text

@app.route('/req_7')
def req_seven():
    # Use environment variable for password in post body
    password = os.getenv('PASSWORD', config.PASSWORD)
    if not password:
        return "Password not configured", 500
    data = {'password': password}
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
    # Use environment variable for value in obscure post body
    value = os.getenv('API_VALUE', config.SOURCE_5)
    if not value:
        return "API value not configured", 500
    data = {'value': value}
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
    # Use environment variable for postgres connection password
    postgres_password = os.getenv('POSTGRES_PASSWORD', config.POSTGRES_PASSWORD)
    if not postgres_password:
        return "Postgres password not configured", 500
    conn = psycopg2.connect(
        host="localhost",
        database="test",
        user="postgres",
        password=postgres_password)
    return conn

@app.route('/red_1')
def red_one():
    # Use environment variable for redis connection password
    redis_password = os.getenv('REDIS_PASSWORD', config.SOURCE_2)
    if not redis_password:
        return "Redis password not configured", 500
    redis_db = redis.StrictRedis(host="localhost", port=6379, db=0, password=redis_password)
    return redis_db

@app.route('/red_2')
def red_2():
    # Use environment variable for redis connection password
    redis_password = os.getenv('REDIS_PASSWORD', config.REDIS_PASSWORD)
    if not redis_password:
        return "Redis password not configured", 500
    redis_db = redis.StrictRedis(host="localhost", port=6379, db=0, password=redis_password)
    return redis_db

@app.route('/')
def entry_point():
    return 'Hello World!'

if __name__ == '__main__':
    # Disable debug mode in production for security
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)