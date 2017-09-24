import socketserver
from time import ctime


class EchoTCPHandler(socketserver.BaseRequestHandler):
    BUFSIZ = 1024

    def handle(self):
        while True:
            data = self.request.recv(self.BUFSIZ)
            if not data:
                break
            data = '[{time}] {data}'.format(time=ctime(), data=data.decode('utf-8'))
            print("{} wrote:".format(self.client_address[0]))
            print(data)
            data = data.encode('utf-8')
            self.request.sendall(data)


class EchoStreamTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            data = self.rfile.readline().strip()
            if not data:
                break
            data = '[{time}] {data}'.format(time=ctime(), data=data.decode('utf-8'))
            print("{} wrote:".format(self.client_address[0]))
            print(data)
            data = data.encode('utf-8')
            self.wfile.write(data)


if __name__ == '__main__':
    HOST, PORT = 'localhost', 21568

    with socketserver.TCPServer((HOST, PORT), EchoStreamTCPHandler) as server:
        server.serve_forever()
