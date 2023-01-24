class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = list(sequence)
        self.number = number
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.number:
            raise StopIteration

        current_letter = self.sequence[self.i % len(self.sequence)]
        self.i += 1
        return current_letter

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

