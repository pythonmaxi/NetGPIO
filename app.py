#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 12:56:16 2020

@author: maxi
"""
from flask import Flask, render_template, request, jsonify
import json
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)


app = Flask(__name__)
path = '/'.join(__file__.split('/')[:-1]) + '/'

# %% Setup gpio varibles
gpio_file = open(path + 'gpios.json', 'r')
gpios = json.loads(gpio_file.read())
gpios = gpios['gpios']
gpio_file.close()

# %% Init the GPIO'S
for gpio_pin in gpios.keys():
    gpio.setup(gpios[gpio_pin]['gpio'], gpio.OUT)


# %% Function to check gpio state
def processGPIOstate(gpio_dict):
    # check if GPIO's are on
    for gpio_pin in gpios.keys():
        state = gpio.input(gpio_dict[gpio_pin]['gpio'])
        if gpio_dict[gpio_pin]['reverse']:
            gpio_dict[gpio_pin]['state'] = not state
        else:
            gpio_dict[gpio_pin]['state'] = state
    return gpio_dict


# %% The home website
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        gpioProcessed = processGPIOstate(gpios)
        data = {
            'gpios': gpioProcessed,
            'gpioList': list(gpioProcessed.keys())
            }
        return render_template('home.html', **data)
    else:
        pin = int(request.json['pin'])
        name = request.json['name']
        if processGPIOstate(gpios)[name]['reverse']:
            new_state = not request.json['state']
        else:
            new_state = request.json['state']
        gpio.output(int(pin), new_state)
        return 'ok'


@app.route('/state', methods=['POST'])
def wait():
    return jsonify(processGPIOstate(gpios))


# %% Start server if main
if __name__ == '__main__':
    app.run(debug=True, port=8080, host='localhost')
    gpio.cleanup()
