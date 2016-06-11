import os
import http.server
import socketserver

OUTPUT_PATH = os.path.abspath(os.path.join(os.getcwd(), "example", "output"))
ADDRESS = "127.0.0.1"
PORT = 8080

os.chdir(OUTPUT_PATH) # Change cwd
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer((ADDRESS, PORT), Handler)
print("serve: Serving at ", ADDRESS + ":" + str(PORT))
httpd.serve_forever()