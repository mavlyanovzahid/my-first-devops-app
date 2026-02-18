from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>DevOps Transformation in Progress!</h1>")

print("Server starting on port 8080...")
server = HTTPServer(('0.0.0.0', 8080), MyHandler)
server.serve_forever()
