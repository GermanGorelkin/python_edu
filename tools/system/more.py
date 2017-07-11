def getreply():
    if sys.stdin.isatty():
        return input('?')
    else:
        if sys.platform[:3] == 'win':
            pass
        else:
            key = open('/dev/tty').readline()[:-1]
            return key


def more(text: str, numlines: int = 15) -> None:
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and getreply() not in ['y', 'Y']:
            break


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        more(open(file_name).read(), 10)
    else:
        more(sys.stdin.read())
