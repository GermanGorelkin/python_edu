# class FibonacciGenerator:
#     def __init__(self):
#         self.prev = 0
#         self.cur = 1
#
#     def __next__(self):
#         result = self.prev
#         self.prev, self.cur = self.cur, self.prev + self.cur
#         return result
#
#     def __iter__(self):
#         return self
#
# for i in FibonacciGenerator():
#     print(i)
#
#     if i > 100:
#         break


def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur
#
# for i in fibonacci():
#     print(i)
#     if i > 100:
#         break

# fib = fibonacci()
# print(next(fib))
# print(next(fib))


# for num, fib in enumerate(fibonacci()):
#     print('{0}: {1}'.format(num, fib))
#     if num > 9:
#         break

##################################################
# def gen_fun():
#     print('block 1')
#     yield 1
#     print('block 2')
#     yield 2
#     print('end')
#
# for i in gen_fun():
#     print(i)
#
#
# def gen_fun_1():
#     print('block 1')
#     return 1
#
#
# def gen_fun_2():
#     print('block 2')
#     return 2
#
#
# def gen_fun_3():
#     print('end')
#
#
# def gen_fun_end():
#     raise StopIteration


############################################
# def cool_range(start, stop, inc):
#     x = start
#     while x < stop:
#         yield x
#         x += inc
#
# for n in cool_range(1, 5, 0.5):
#     print(n)
# # 1
# # 1.5
# # ...
# # 4.5
#
# print(list(cool_range(0, 2, 0.5)))


# ###############
#
# class Countdown:
#     def __init__(self, start):
#         self.start = start
#
#     def __iter__(self):
#         n = self.start
#         while n > 0:
#             yield n
#             n -= 1
#
#     def __reversed__(self):
#         n = 1
#         while n <= self.start:
#             yield n
#             n += 1
#
#
# cd = Countdown(10)
#
# for i in cd:
#     print(i)
#
#
# for i in reversed(cd):
#     print(i)
#############################################


# (i for i in range(10000000))
# [i for i in range(10000000)]

#################

# def chain(*iterables):
#     for it in iterables:
#         for i in it:
#             yield i
#
# g = chain([1, 2, 3], {'A', 'B', 'C'}, '...')
# print(list(g))
# # [1, 2, 3, 'A', 'B', 'C', '.', '.', '.']
#
# def chain(*iterables):
#     for it in iterables:
#         yield from it
#
# g = chain([1, 2, 3], {'A', 'B', 'C'}, '...')
# print(list(g))
# [1, 2, 3, 'A', 'B', 'C', '.', '.', '.']
#

# from collections import Iterable
#
# def flatten(items, ignore_types=(str, bytes)):
#     """
#       str, bytes - являются итерируемыми объектами,
#        но их хотим возвращать целыми
#     """
#     for x in items:
#         if isinstance(x, Iterable) and not isinstance(x, ignore_types):
#             yield from flatten(x)
#         else:
#             yield x
#
# items = [1, 2, [3, 4, [5, 6], 7], 8, ('A', {'B', 'C'})]
#
# for x in flatten(items):
#     print(x)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# A
# C
# B