
def get_args(args: tuple) -> list:
    value = []
    if len(args) == 1:
        for item in args[0]:
            value.append(item)
    else:
        for item in args:
            value.append(item)
    return value


class DmSetError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class DmSet:
    def __init__(self, *args):
        self.values = []

        items = get_args(args)

        for item in items:
            if not (item in self.values):
                self.values.append(item)

        self.values.sort(key=lambda x: (isinstance(x, int), x))

    def add(self, other):
        if not (other in self.values):
            self.values.append(other)
        self.values.sort(key=lambda x: (isinstance(x, int), x))
        return self.values

    def remove(self, other):
        if other in self.values:
            self.values.remove(other)
            self.values.sort(key=lambda x: (isinstance(x, int), x))
            return self.values
        else:
            raise ItemNotFoundError

    def contains(self, other):
        return other in self.values

    def union(self, *args):
        other = get_args(args)
        for item in other:
            if not (item in self.values):
                self.values.append(item)
        self.values.sort(key=lambda x: (isinstance(x, int), x))

    def intersection(self, *args):
        other = get_args(args)
        new = []
        for item in other:
            if item in self.values:
                new.append(item)
        self.values = new
        self.values.sort(key=lambda x: (isinstance(x, int), x))

    def difference(self, *args):
        other = get_args(args)
        for value in self.values:
            if value in other:
                self.remove(value)
        self.values.sort(key=lambda x: (isinstance(x, int), x))

    def complement(self, *args):
        other = get_args(args)
        new = []
        for value in other:
            if not (value in self.values):
                new.append(value)
        self.values = new
        self.values.sort(key=lambda x: (isinstance(x, int), x))

    def __iter__(self) -> iter:
        return iter(self.values)

    def __repr__(self):
        return f'({str(self.values)[1:-1]})'


def main():
    set1 = DmSet(1, 2, 2, 3)
    print(set1)
    set1.add(4)
    print(set1)
    set1.remove(4)
    print(set1)
    print(set1.contains(4))
    set1.union([3, 4, 5])
    print(set1)
    set2 = DmSet(1, 2, 3)
    set2.intersection(DmSet(3, 4, 5))
    print(set2)
    set3 = DmSet([1, 2, 3])
    set3.difference(3, 4, 5)
    print(set3)
    set4 = DmSet(1, 2, 3)
    set4.complement([1, 2, 3, 4, 5])
    print(set4)


if __name__ == '__main__':
    main()

ItemNotFoundError = DmSetError("DmSet.remove(x): x does not exist")
