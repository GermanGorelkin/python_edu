# пример использования property
# attribute = property(fget, fset, fdel, doc)


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def del_name(self):
        print('del name', self.name)
        del self._name

    name = property(get_name, set_name, del_name)


class SubPerson(Person):
    pass


bob = Person('bob')
print(bob.name)
bob.name = 'Bobi'
print(bob.name)
del bob.name
print()
tod = Person('tod')
print(tod.name)
tod.name = 'Todi'
print(tod.name)
del tod.name

print('-' * 10)


# -------------------------------
# вычисляемые атрибуты
class PropSquare:
    def __init__(self, start):
        self.value = start

    def get_x(self):
        return self.value ** 2

    def set_x(self, value):
        self.value = value

    X = property(get_x, set_x)


P = PropSquare(3)
print('P = PropSquare(3)')
Q = PropSquare(32)
print('Q = PropSquare(32)')

print('P.X = ', P.X)
P.X = 4
print('P.X = 4')
print('P.X = ', P.X)
print('P.Q = ', Q.X)

print('-' * 10)


# -------------------------------
# декоратор
class PersonDec:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        print('deleter name', self.name)
        del self._name


bob = PersonDec('bob dec')
print(bob.name)
bob.name = 'Bobi Dec'
print(bob.name)
del bob.name
