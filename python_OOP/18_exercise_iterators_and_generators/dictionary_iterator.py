class dictionary_iter:
    def __init__(self, data):
        self.data = data
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.data):
            current_el = list(self.data.items())[self.i]
            self.i += 1
            return current_el

        raise StopIteration


result = dictionary_iter({1: "1", 2: "2", 3: "3"})
for x in result:
    print(x)
