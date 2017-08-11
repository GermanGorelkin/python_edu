# registry = []
#
#
# def register(func):
#     print('running register(%s)' % func)
#     registry.append(func)
#     return func
#
#
# @register
# def f1():
#     print('running f1()')
#
#
# def f2():
#     print('running f2()')
# f2 = register(f2)   # эквивалентно @register
#
#
# def f3():
#     print('running f3()')
#
#
# def main():
#     print('running main()')
#     print('registry -> ', registry)
#     f1()
#     f2()
#     f3()
#
##############################################
# if __name__ == '__main__':
#     main()

# @d1
# @d2
# def f():
#     print('f')

##############################################
# import time
#
#
# def clock(func):
#     """
#     Фактически функция clocked заменит собой декорированую функцию.
#     При вызове clocked вызывает декорированую функцию и возращает результат этой функции.
#     При этом поевляется возможность добавить дополнительную логику
#         до и/или полсе вызова декорированной функции.
#     """
#     def clocked(*args, **kwargs):
#         t0 = time.time()
#
#         result = func(*args, **kwargs)  # вызов декорированной функции
#
#         elapsed = time.time() - t0
#         name = func.__name__
#         arg_1st = []
#         if args:
#             arg_1st.append(', '.join(repr(arg) for arg in args))
#         if kwargs:
#             pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
#             arg_1st.append(', '.join(pairs))
#         arg_str = ', '.join(arg_1st)
#         print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
#         return result
#     return clocked
#
#
# @clock
# def factorial(n):
#     return 1 if n < 2 else n * factorial(n-1)
# # factorial = clock(factorial)
#
# print('100! =', factorial(100))  # фактически вызываем clocked(100)

####################################################

# import time
#
# DEFAULT_FMT = '[{elapsed:0.8f}s] {name} ({arg_str}) -> {result}'
#
#
# def clock(fmt=DEFAULT_FMT):
#
#     def decorate(func):
#         def clocked(*args, **kwargs):
#             t0 = time.time()
#             result = func(*args, **kwargs)
#             elapsed = time.time() - t0
#             name = func.__name__
#             arg_1st = []
#             if args:
#                 arg_1st.append(', '.join(repr(arg) for arg in args))
#             if kwargs:
#                 pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
#                 arg_1st.append(', '.join(pairs))
#             arg_str = ', '.join(arg_1st)
#             print(fmt.format(**locals()))
#             return result
#         return clocked
#
#     return decorate
#
#
# @clock()
# def factorial(n):
#     return 1 if n < 2 else n * factorial(n-1)
#
#
# def factorial2(n):
#     return 1 if n < 2 else n * factorial2(n-1)
#
# factorial2 = clock('{name}: {elapsed}s')(factorial2)
#
# print('6! =', factorial(6))
#
# print('6! =', factorial2(6))
#
#
###############################################################
#
# route_map = {}
#
#
# def route(path):
#     def decorate(func):
#         route_map[path] = func
#         return func
#
#     return decorate
#
#
# @route('/users')
# def users():
#     return 'all users'
#
#
# @route('/shops')
# def shops():
#     return 'all shops'
#
#
# from urllib.parse import urlparse
#
# url = urlparse('http://example.com/users')
# handler = route_map.get(url.path)
# if handler:
#     print(handler())
#
# url = urlparse('http://example.com/shops')
# handler = route_map.get(url.path)
# if handler:
#     print(handler())
