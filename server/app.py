#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
import os
import re
import subprocess

import config
import printing

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    auth = flask.request.authorization
    for username, password in config.USERS:
        if auth and auth.username == username and auth.password == password:
            break
    else:
        return flask.Response(
            '<h1>Invalid Credentials</h1><p>Please login with your contest login and password.</p>',
            401,
            {'WWW-Authenticate': 'Basic realm="Enter your contest credentials"'}
        )

    result = None
    if flask.request.method == 'POST':
        source = flask.request.form.get('source', '').strip()
        if source == '':
            result = {'type': 'error', 'message': 'Please enter your source in the field'}
        else:
            printing.run_threaded(username, source)
            result = {'type': 'success', 'message': 'Your source has been accepted for printing. Please wait'}
    return flask.render_template('index.html', username=username, result=result)


@app.route('/api/jobs', methods=['GET', 'POST'])
def jobs():
    if flask.request.headers['Authorization'] != f'Bearer {config.TOKEN}':
        return flask.jsonify({'error': 'not-authorized'}), 403
 
    if flask.request.method == 'POST':
        filename = flask.request.form.get('filename', '')
        path = os.path.join('static/pdfs', filename)
        if not re.fullmatch(r'^[a-z0-9-]+\.pdf$', filename) or not os.path.exists(path):
            return flask.jsonify({'error': 'bad-file'}), 403
        os.remove(path)
        return flask.jsonify({'result': 'ok'})
    else:
        return flask.jsonify({'result': os.listdir('static/pdfs')})


if __name__ == '__main__':
    if not os.path.exists('static/pdfs'):
        os.mkdir('static/pdfs')
    app.run(host=config.HOST, port=config.PORT)
