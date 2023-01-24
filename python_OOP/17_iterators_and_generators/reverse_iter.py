class reverse_iter:
    def __init__(self, obj):
        self.obj = obj
        self.start = len(obj)
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            self.start -= 1
            return self.obj[self.start]
        else:
            raise StopIteration

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

