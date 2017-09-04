"""
    1. Создание экземпляра Thread с передачей функции
    2. Создание экземпляра Thread и передача вызываемого экземпляра класса
    3. Формирование подкласса Thread и создание экземпляра подкласса
"""

from threading import Thread
import time


def counter(th_id, count):
    for i in range(count):
        print('[{0}] => {1}'.format(th_id, i))
        time.sleep(1)

"""
    Создание экземпляра Thread с передачей функции
"""
# th = Thread(target=counter, args=(1, 5))
# th.start()
# th.join()
#
# print('Main thread exiting.')
#################


"""
    Создание экземпляра Thread и передача вызываемого экземпляра класса
"""
#
#
# class ThreadFunc:
#     def __init__(self, func, args, name=''):
#         self.func = func
#         self.args = args
#         self.name = name
#
#     def __call__(self, *args, **kwargs):
#         self.func(*self.args)
#
# th = Thread(target=
#             ThreadFunc(func=counter, args=(1, 5), name=counter.__name__))
# th.start()
# th.join()
#
# print('Main thread exiting.')
##############################


"""
    Формирование подкласса Thread и создание экземпляра подкласса.
    Добавлена возможность получить результат выполнения функции.
    Добавлена функция callback
"""


def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


class MyThread(Thread):
    def __init__(self, func, args, name='', callback=None):
        Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
        self.callback = callback

    def run(self):
        self.result = self.func(*self.args)
        if self.callback:
            self.callback(self.result)

    def result(self):
        return self.result


th = MyThread(func=fib, args=(10, ), name=fib.__name__,
              callback=lambda r: print('callback. result: {}'.format(r)))
th.start()
th.join()

print('result: {}'.format(th.result))

print('Main thread exiting.')
