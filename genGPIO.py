#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:15:26 2020

@author: maxi
"""
import json

dic = {'gpios': {}}

if input('Use reverse power? [y/n]') == 'y':
    dic['reverse'] = True

else:
    dic['reverse'] = False

while True:
    inp = input('GPIO name: ')
    if inp == 'done':
        break
    else:
        dic['gpios'][inp] = {}
        dic['gpios'][inp]['gpio'] = int(input('GPIO number: '))
with open('gpios.json', 'w') as gpios:
    gpios.write(json.dumps(dic, sort_keys=True, indent=4))
