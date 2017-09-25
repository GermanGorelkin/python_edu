import threading
import socketserver
from time import ctime


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    BUFSIZ = 1024

    def handle(self):
        while True:
            data = self.request.recv(self.BUFSIZ)
            if not data:
                break
            cur_thread = threading.current_thread()
            data = '[{cur_thread}][{time}] {data}'.format(
                cur_thread=cur_thread, time=ctime(), data=data.decode('utf-8'))
            print("{} wrote:".format(self.client_address[0]))
            print(data)
            data = data.encode('utf-8')
            self.request.sendall(data)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == '__main__':
    HOST, PORT = 'localhost', 21568

    with ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler) as server:
        server.serve_forever()
