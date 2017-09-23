import socket
from time import ctime

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

print(socket.gethostbyname(socket.gethostname()))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcpServSock:
    tcpServSock.bind(ADDR)
    tcpServSock.listen()
    print(tcpServSock.getsockname())

    while True:
        print('waiting for connection...')
        tcpClisock, addr = tcpServSock.accept()
        print('...connected from:', addr)

        with tcpClisock:
            while True:
                data = tcpClisock.recv(BUFSIZ)
                if not data:
                    break
                data = '[{time}] {data}'.format(time=ctime(), data=data.decode('utf-8'))
                print(data)
                data = data.encode('utf-8')
                tcpClisock.send(data)

