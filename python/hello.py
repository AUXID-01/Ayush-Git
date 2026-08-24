from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, World!")

server = HTTPServer(("0.0.0.0", 80), Handler)

print("Server running on port 80")
server.serve_forever()