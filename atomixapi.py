import http.server
import socketserver

class customHttpHandler(http.server.BaseHTTPRequestHandler):
    
    routes = {}
    
    def do_GET(self):
        if self.path in self.routes:
            handler = self.routes[self.path]
            handler_res = handler()

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(handler_res.encode('utf-8'))
            
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("404")

class AtomixAPI():
    def __init__(self):
        pass
            
    def get(self, path_, handler_):
        customHttpHandler.routes[path_] = handler_
            
    @classmethod
    def listen(cls, port):
        with socketserver.TCPServer(("", port), customHttpHandler) as httpd:
            print(f"Server Up at: http://localhost:{port}/")
            print(f"Let's Goooo!")
            httpd.serve_forever()
