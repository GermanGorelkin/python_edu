import time


def clock(func):
    """
    Фактически функция clocked заменит собой декорированую функцию.
    При вызове clocked вызывает декорированую функцию и возращает результат этой функции.
    При этом поевляется возможность добавить дополнительную логику
        до и/или полсе вызова декорированной функции.
    """
    def clocked(*args, **kwargs):
        t0 = time.time()

        result = func(*args, **kwargs)  # вызов декорированной функции

        elapsed = time.time() - t0
        name = func.__name__
        arg_1st = []
        if args:
            arg_1st.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_1st.append(', '.join(pairs))
        arg_str = ', '.join(arg_1st)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


# @clock
# def factorial(n):
#     if n < 2:
#         return n
#     return factorial(n-2) + factorial(n-1)
#
# print('20! =', factorial(20))

######################
# _fib_cache = {1: 1, 2: 1}
#
#
# @clock
# def mem_factorial(n):
#     result = _fib_cache.get(n)
#     if result is None:
#         result = mem_factorial(n-2) + mem_factorial(n-1)
#         _fib_cache[n] = result
#     return result
#
# print('200! =', mem_factorial(200))
#
############################################################

# def memoize(f):
#     cache = {}
#
#     def decorate(*args):
#         if args in cache:
#             return cache[args]
#         else:
#             cache[args] = f(*args)
#             return cache[args]
#     return decorate
#
# # def memoize(f):
# #     cache = {}
# #     return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]
#
# # def memoize(f):
# #     cache = {}
# #
# #     def decorate(*args, **kwargs):
# #         key = (tuple(args), hash(tuple(sorted(kwargs.items()))))
# #         if key not in cache:
# #             cache[key] = f(*args, **kwargs)
# #         return cache[key]
# #
# #     return decorate
#
#
# @clock
# @memoize
# def mem_factorial(n):
#     if n < 2:
#         return n
#     return mem_factorial(n-2) + mem_factorial(n-1)
#
# print('20! =', mem_factorial(20))

############################################################

# from functools import lru_cache
#
#
# @clock
# @lru_cache()
# def mem_factorial(n):
#     if n < 2:
#         return n
#     return mem_factorial(n-2) + mem_factorial(n-1)
#
# print('20! =', mem_factorial(20))
