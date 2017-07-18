class Descriptor:
    """
    self - экземпляр дескриптора
    instance - экземпляр клиенского класса
    owner - клиенский класс
    """

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


# Name - вложенный дескриптор для класса Person
class Person:
    def __init__(self, name):
        self._name = name

    class Name:
        def __get__(self, instance, owner):
            return instance._name

        def __set__(self, instance, value):
            instance._name = value

        def __delete__(self, instance):
            print('delete name', instance._name)
            del instance._name

    name = Name()


bob = Person('bob dec')
print(bob.name)
bob.name = 'Bobi Dec'
print(bob.name)
del bob.name

print('-' * 10)


# Вычисляемые атрибуты
# Значения дескриптор хранит у себя
class DescSquare:
    def __init__(self, start):
        self.value = start

    def __get__(self, instance, owner):
        return self.value ** 2

    def __set__(self, instance, value):
        self.value = value


class Client1:
    X = DescSquare(2)
    Y = DescSquare(3)


class Client2:
    X = DescSquare(32)


c1 = Client1()
c2 = Client2()
print('c1.X = {0}, c1.Y = {1}'.format(c1.X, c1.Y))
print('c2.X = ', c2.X)
c1.Y = 10
print('c1.Y = 10')
print('c1.Y = ', c1.Y)

print('-' * 10)


# Простая имитация свойства
class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)  # аргумент self

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    name = Property(get_name, set_name)


bob = Person('bob')
print(bob.name)
bob.name = 'Bobi'
print(bob.name)
# del bob.name    # delete не реализован. вызовит ошибку
print()
tod = Person('tod')
print(tod.name)
tod.name = 'Todi'
print(tod.name)
