class WatchList:
    def __init__(self):
        self.data = []

    def __enter__(self):
        """
        Значение после as
        """
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('len list = {len}'.format(len=len(self.data)))


with WatchList() as d:
    d.append(1)
    d.append(2)

