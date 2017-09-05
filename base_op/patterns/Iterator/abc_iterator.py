import collections.abc

# collections.abc.Iterable
# collections.abc.Iterator


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


if __name__ == '__main__':
    collection = [1, 2, 5, 6, 8]
    aggregate = ListCollection(collection)

    for item in aggregate:
        print(item)

    print("*" * 50)

    itr = iter(aggregate)
    while True:
        try:
            print(next(itr))
        except StopIteration:
            break
