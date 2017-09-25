# def make_multiplier_of(n):
#     """принимает n и создает функцию(multiplier) которая будет домножать n на аргумент(x) из созданной функции"""
#
#     def multiplier(x):
#         """у обьекта multiplier будет ссылка на переменную n,
#            к которой она сможет образаться уже после создания"""
#         return x * n
#
#     return multiplier
#
# times3 = make_multiplier_of(3)
# times5 = make_multiplier_of(5)
#
# print(times3(9))
# print(times5(3))
# print(times5(times3(2)))
#
# # ----
# print('все переменные: ', times3.__code__.co_varnames)
# print('свободные из внешней функции: ', times3.__code__.co_freevars)
# for indx, fv_name in enumerate(times3.__code__.co_freevars):
#     print('{0} = {1}'.format(fv_name, times3.__closure__[indx].cell_contents))
#
# print('все переменные: ', times5.__code__.co_varnames)
# print('свободные из внешней функции: ', times5.__code__.co_freevars)
# for indx, fv_name in enumerate(times5.__code__.co_freevars):
#     print('{0} = {1}'.format(fv_name, times5.__closure__[indx].cell_contents))
#

#
# def make_averanger():
#     count = 0
#     total = 0
#
#     def averanger(new_value):
#         nonlocal count, total
#         count += 1
#         total += new_value
#         return total / count
#     return averanger
#
# avg = make_averanger()
# print(avg(10))
# print(avg(20))
# print(avg(100))


# def makeActions():
#     acts = []
#     for i in range(5):
#         acts.append(lambda x: i ** x)
#     return acts
#
# for act in makeActions():
#     print(act(1), end=', ')
#
# print()
#
#
# def makeActions():
#     acts = []
#     for i in range(5):
#         acts.append(lambda x, i=i: i ** x)
#     return acts
#
# for act in makeActions():
#     print(act(1), end=', ')
#
#
# print()
#
#
# def makeActions():
#     acts = []
#     for i in range(5):
#         def func(x, i=i):
#             return x * i
#         acts.append(func)
#     return acts
#
# for act in makeActions():
#     print(act(1), end=', ')


# def func(v, x=[]):
#     x.append(v)
#     print(x)
#
# for i in range(5):
#     func(i)
