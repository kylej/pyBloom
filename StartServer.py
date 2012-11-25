#!/usr/bin/env python
import BaseHTTPServer
from bloomfilter import BloomFilter
server_host = 'localhost'
server_port = 8800
bloom = BloomFilter(m=1024*1024*1024*2,k=4)

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):        
        s.send_response(200) 
        s.end_headers()
		#quick and dirty
        id=s.path[s.path.rfind('/')+1:]
        dup = bloom.add(id)
        out=1
        if dup==True:
            out=0       	
        s.wfile.write(out)        

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((server_host, server_port), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    fd.close()

