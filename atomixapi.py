from urllib.parse import urlparse, parse_qs
import http.server
import socketserver
import json as json_converter
import re

class customHttpHandler(http.server.BaseHTTPRequestHandler):
    
    routes = {}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        
        params = re.findall('\d', path)
        
        for route in self.routes:
            print(route)
            if "/:id" in route:
                self.routes[path] = self.routes[route]
                
        if path in self.routes:
            handler = self.routes[path]
            get_query = parse_qs(parsed_url.query)
            
            query = {}
            
            for q in get_query:
                query[q] = get_query[q][0]
            
            req = {
                "path": path,
                "query": query,
                "params": params
            }

            handler(req, self)

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("404".encode('utf-8'))
            
    def send(self, res_):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(res_.encode('utf-8'))
        
    def json(self, res_):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json_converter.dumps(res_).encode('utf-8'))
        

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

