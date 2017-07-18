class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, item):
        print('Trace:', item)
        return getattr(self.wrapped, item)


class Person:
    def __init__(self, lname, fname):
        self.lname = lname
        self.fname = fname

    def get_full_name(self):
        return self.lname + ' ' + self.fname


p = Person('Last', 'First')
wp = Wrapper(p)
print(wp.lname)
print(wp.fname)
print(wp.get_full_name())
# print(wp.test) # AttributeError

print('-' * 10)


class Person:
    # X = 100

    def __init__(self, name):
        print('__init__')
        self._name = name  # вызов __setattr__

    def __getattr__(self, attr):  # вызов отсутствущих атрибутов
        print('__getattr__')
        if attr == 'name':
            return self._name
        else:
            raise AttributeError(attr)

    def __getattribute__(self, attr):
        print('__getattribute__', self, attr)
        if attr == 'name':
            attr = '_name'
        return object.__getattribute__(self, attr)  # предотвращаем зацикливание

    def __setattr__(self, attr, value):
        print('__setattr__')
        if attr == 'name':
            attr = '_name'
        self.__dict__[attr] = value  # предотвращаем зацикливание

    def __delete__(self, attr):
        print('__delete__')
        if attr == 'name':
            attr = '_name'
        del self.__dict__[attr]  # предотвращаем зацикливание

p = Person('German')
print(p.name)
