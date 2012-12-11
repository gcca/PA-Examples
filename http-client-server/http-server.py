#!/usr/bin/python
import time
import sys
import BaseHTTPServer

if len(sys.argv) != 3:
	print "Usage: http-server.py <hostname> <port>"
	print "Hostname field should be actual hostname or localhost"
	sys.exit(0)

port = int(sys.argv[2])	
host = sys.argv[1]

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Test Page</title></head>")
        s.wfile.write("<body><p>This is a test.</p>")
        s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        s.wfile.write("</body></html>")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((host, port), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (host, port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (host, port)