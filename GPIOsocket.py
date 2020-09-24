#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:23:51 2020

@author: maxi
"""
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket


class GPIOsocket(tornado.websocket.WebSocketHandler):
    clients = set()

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def open(self):
        self.clients.add(self)
        print('New client connected')

    def on_message(self, message):
        if str(message) == 'changed':
            for client in self.clients:
                client.write_message(message)
        else:
            self.write_message('undefined')

    def on_close(self):
        self.clients.remove(self)

    def check_origin(self, origin):
        return True


application = tornado.web.Application([(r'/socket', GPIOsocket)])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    host = socket.gethostbyname(socket.gethostname())
    print('Started server')
    tornado.ioloop.IOLoop.instance().start()
