#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 12:56:16 2020

@author: maxi
"""
from flask import Flask, render_template, request
import json

app = Flask(__name__)


gpiofile = open('gpios.json', 'r')
gpios = json.loads(gpiofile.read())['gpios']
gpiofile.close()


def processGPIOstate(gpios):
    # check if GPIO's are on
    return gpios

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = {
            'gpios': processGPIOstate(gpios)
            }
        return render_template('home.html', **data)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
