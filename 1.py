from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloWorldRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"hello, world!")
    
print("server is running no http://localhost:8000")
httpd = HTTPServer(("localhost", 8000), HelloWorldRequestHandler)
httpd.serve_forever()