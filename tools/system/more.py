def more(text: str, numlines: int = 15) -> None:
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and input('More?') not in ['y', 'Y']:
            break


if __name__ == '__main__':
    import sys
    if sys.argv.count() > 1:
        file_name = sys.argv[1]
        more(open(file_name).read(), 10)
