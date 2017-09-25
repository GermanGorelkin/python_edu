class ProgrammingLanguages:

    _name = ("Python", "Golang", "C#", "C", "C++", "Java", "SQL", "JS")

    def __init__(self, first=None):
        self.index = (-1 if first is None else
                      ProgrammingLanguages._name.index(first) - 1)

    def __call__(self):
        self.index += 1
        if self.index < len(ProgrammingLanguages._name):
            return ProgrammingLanguages._name[self.index]
        raise StopIteration


class FibonacciNumber:
    def __init__(self, num=1000):
        self.index = num
        self.prev = 0
        self.cur = 1

    def __call__(self):
        self.index -= 1
        if self.index > 0:
            self.prev, self.cur = self.cur, self.cur + self.prev
            return self.prev
        raise StopIteration


from random import randint

def d6():
    return randint(1, 6)


if __name__ == '__main__':
    for lang in iter(ProgrammingLanguages("C#"), None):
        print(lang)

    print("-" * 50)

    for lang in iter(ProgrammingLanguages(), "C"):
        print(lang)

    print("-" * 50)

    for num, fn in enumerate(iter(FibonacciNumber(), 89), 1):
        print('{0}: {1}'.format(num, fn))

    print("-" * 50)

    for roll in iter(d6, 6):
        print(roll)

    # читаем файл до пустой строки
    # with open('mydata.txt') as fp:
    #     for line in iter(fp.readline, ''):
    #         print(line)
