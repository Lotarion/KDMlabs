def get_args(args: tuple) -> list:
    value = []
    if len(args) == 1:
        for item in args[0]:
            value.append(item)
    else:
        for item in args:
            value.append(item)
    return value


class DmSet:
    def __init__(self, *args):
        self.values = []

        items = get_args(args)

        for item in items:
            if not(item in self.values):
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

    def contains(self, other):
        return other in self.values

    def __str__(self):
        return self.values

    # def __iter__(self) -> iter:
    #     return iter(self.values)


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
