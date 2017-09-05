import abc


class Aggregate(abc.ABC):

    @abc.abstractmethod
    def iterator(self):
        """
        Возращает итератор
        """
        pass


class Iterator(abc.ABC):
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    @abc.abstractmethod
    def first(self):
        """
        Возращает итератор к началу агрегата
        """
        pass

    @abc.abstractmethod
    def next(self):
        """
        Переходит на следующий элемент агрегата.
        Вызывает ошибку StopIteration, если достигнут конец последовательности.
        """
        pass

    @abc.abstractmethod
    def current(self):
        """
        Возвращает текущий элемент
        """
        pass


class ListIterator(Iterator):
    def __init__(self, collection, cursor):
        super().__init__(collection, cursor)

    def first(self):
        self._cursor = -1

    def next(self):
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1

    def current(self):
        return self._collection[self._cursor]


class ListCollection(Aggregate):
    def __init__(self, collection):
        self._collection = collection

    def iterator(self):
        return ListIterator(self._collection, -1)


if __name__ == '__main__':
    collection = [1, 2, 5, 6, 8]
    aggregate = ListCollection(collection)
    itr = aggregate.iterator()

    while True:
        try:
            itr.next()
        except StopIteration:
            break
        print(itr.current())

        itr.first()

    while True:
        try:
            itr.next()
        except StopIteration:
            break
        print(itr.current())
