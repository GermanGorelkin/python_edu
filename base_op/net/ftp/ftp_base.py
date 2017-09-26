import ftplib
import socket
from collections import namedtuple

HOST = ''
USER = ''
PASSWORD = ''
DIRN = ''
FILE = ''


def main():
    with ftplib.FTP() as ftp:
        try:
            ftp.connect(host=HOST)
        except (socket.error, socket.gaierror) as e:
            print('ERROR: cannot reach "{HOST}"'.format(HOST=HOST))
            return
        print('*** Connected to host "{HOST}"'.format(HOST=HOST))

        try:
            ftp.login(user=USER, passwd=PASSWORD)
        except ftplib.error_perm:
            print('ERROR: cannot login')
            return

        # files = ftp.nlst()
        # for file in files:
        #
        #     file_size = 0# ftp.size(file)
        #     print('{name} : {size}'.format(name=file, size=file_size))

        # ls = []
        # ftp.retrlines('MLSD', ls.append)
        # for entry in ls:
        #     parser_mlsd(entry)

        # upload file
        # filename = "test.txt"
        # ftp.storbinary("STOR " + filename, open(filename, 'rb'))


        # download file
        # filename = "test.txt"
        # ftp.retrbinary("RETR " + filename, open("dtext.txt", 'wb').write)



FTPFile = namedtuple('FTPFile', ['type', 'modify', 'size', 'name'])


def parser_mlsd(line):
    file_prop = line.split(';')
    # print(file_prop)
    f_type = file_prop[0][5:]
    modify = file_prop[1][7:]
    size = 0
    if len(file_prop) == 4:
        size = file_prop[2][5:]
        name = file_prop[3]
    else:
        name = file_prop[2]
    file = FTPFile(f_type, modify, size, name.strip())
    print(file)


if __name__ == '__main__':
    main()

