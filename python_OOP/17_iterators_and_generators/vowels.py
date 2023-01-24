class vowels:
    def __init__(self, string):
        self.string = string
        self.start = 0

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        try:
            while True:
                current_letter = self.string[self.start]
                self.start += 1
                if current_letter.lower() in "aeiuyo":
                    return current_letter
        except IndexError:
            raise StopIteration



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
