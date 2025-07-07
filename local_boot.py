import update
import http.server
import socketserver


PORT = 8000  # You can change the port number here

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("Browser at http://localhost:8000")
    httpd.serve_forever()

