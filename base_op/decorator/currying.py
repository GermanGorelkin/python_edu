# def greet(greeting, name):
#     print(greeting + ', ' + name)
#
# greet('Hello', 'German')
#
#################################################
# def greet_curried(greeting):
#     def greet(name):
#         print(greeting + ', ' + name)
#     return greet
#
# greet_hello = greet_curried('Hello')
#
# greet_hello('German')
# greet_hello('Ivan')
#
# # или сразу через greet_curried
# greet_curried('Hi')('Roma')
#
#######################################
# def greet_deeply_curried(greeting):
#     def w_separator(separator):
#         def w_emphasis(emphasis):
#             def w_name(name):
#                 print(greeting + separator + name + emphasis)
#             return w_name
#         return w_emphasis
#     return w_separator

# greet_deeply_curried = lambda greeting: lambda separator: lambda emphasis: lambda name: \
#     print(greeting + separator + name + emphasis)
#
# greet = greet_deeply_curried("Hello")("...")(".")
# greet('German')
# greet('Ivan')
#
################################
# from functools import partial
#
#
# def greet(greeting, separator, emphasis, name):
#     print(greeting + separator + name + emphasis)
#
# newfunc = partial(greet, greeting='Hello', separator=',', emphasis='.')
# newfunc(name='German')
# newfunc(name='Ivan')
#
# newfunc2 = partial(greet, greeting='Hello', emphasis='.')
# newfunc2(name='German', separator='...')
# newfunc2(name='Ivan', separator='..')
#
########################################
# from functools import partial
#
#
# def makeActions():
#     acts = []
#     for i in range(5):
#         def func(x, y):
#             return x * y
#         acts.append(partial(func, y=i))
#         # acts.append(partial(lambda x, y: x * y, y=i)) # через lambda
#     # return [partial(lambda x, y: x * y, y=i) for i in range(5)] # через генератор списка
#     return acts
#
# for act in makeActions():
#     print(act(1), end=', ')


