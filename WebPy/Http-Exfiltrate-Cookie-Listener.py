#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import logging

PORT = 80

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
    

Handler = GetHandler
httpd = SocketServer.TCPServer(("0.0.0.0", PORT), Handler)

httpd.serve_forever()