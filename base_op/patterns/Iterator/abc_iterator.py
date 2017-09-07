import collections.abc

# collections.abc.Iterable
# collections.abc.Iterator
# collections.abc.Sequence
# collections.abc.Callable


class ListIterator(collections.abc.Iterator):
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    def __next__(self):
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1
        return self._collection[self._cursor]


class ListCollection(collections.abc.Iterable):
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return ListIterator(self._collection, -1)


class SomeIterable1(collections.abc.Iterable):
    def __iter__(self):
        pass

class SomeIterable2:
    def __iter__(self):
        pass

from string import ascii_letters

class SomeIterable3:
    def __getitem__(self, key):
        return ascii_letters[key]


if __name__ == '__main__':
    collection = [1, 2, 5, 6, 8]
    aggregate = ListCollection(collection)

    # for item in aggregate:
    #     print(item)
    #
    # print("*" * 50)
    #
    # itr = iter(aggregate)
    # while True:
    #     try:
    #         print(next(itr))
    #     except StopIteration:
    #         break

    # itr = iter(aggregate)
    # while True:
    #     item = next(itr, None)
    #     if item is None:
    #         break
    #     print(item)



    # print(isinstance(SomeIterable1(), collections.abc.Iterable))
    # print(isinstance(SomeIterable2(), collections.abc.Iterable))
    #
    # for item in SomeIterable3():
    #     print(item)
