from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler, HTTPServer
import socketserver
import sys


def test(HandlerClass=BaseHTTPRequestHandler,
         ServerClass=HTTPServer, protocol="HTTP/1.0", port=8000, bind=""):

    server_address = (bind, port)

    HandlerClass.protocol_version = protocol
    with ServerClass(server_address, HandlerClass) as httpd:
        sa = httpd.socket.getsockname()
        serve_message = "Serving HTTP on {host} port {port} (http://{host}:{port}/) ..."
        print(serve_message.format(host=sa[0], port=sa[1]))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            sys.exit(0)


class ThreadedHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    pass


if __name__ == '__main__':
    test(HandlerClass=SimpleHTTPRequestHandler, ServerClass=ThreadedHTTPServer)

