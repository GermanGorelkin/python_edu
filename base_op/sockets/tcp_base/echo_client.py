import socket

HOST = '127.0.0.1'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

with socket.socket() as tcpCliSock:
    tcpCliSock.connect(ADDR)

    while True:
        data = input('> ')
        if not data:
            break
        data = (data+"\n").encode('utf-8')
        tcpCliSock.send(data)

        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        data = data.decode('utf-8')
        print('< ', data)


