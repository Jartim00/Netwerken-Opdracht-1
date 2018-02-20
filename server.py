from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import urlparse
import time
from threading import Thread
import os

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Last-Modified', self.date_time_string(time.time()))
        self.end_headers()
        self.wfile.write('<!DOCTYPE html>\n'+
                          '<html>\n'+
                          '<body style="background-color:powderblue;">\n'+
                          '<h1>My first Heading</h1>\n'+
                          '<p>My first paragraph\n'+
                          '</body>\n'+
                          '</html>')

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def serve_on_port(port):
    print "started server on: http://localhost:" + str(port)
    server = ThreadingHTTPServer(("localhost",port), GetHandler)
    server.serve_forever()

if __name__ == '__main__':    
    print "######################## MENU #################################"
    print "Select the mount of clients you'd like."
    print "######################## INTERMISSION #########################"
    inputnumber = input('select number: ')
    print "---------------------------------------------------------------"
    if inputnumber > 0:
        inputnumber = 8000+inputnumber
        for s in range(8000,inputnumber):
            t = Thread(target=serve_on_port, args=[s])
            t.start()
    else:
        print "Wrong input, please try again"
        #os.system('cls' if os.name == 'nt' else 'clear')
