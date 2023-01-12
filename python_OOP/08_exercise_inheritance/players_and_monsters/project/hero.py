class Hero:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __str__(self):
        return f"{self.username} of type {type(self).__name__} has level {self.level}"
    #self.__class__.__name__


d = Hero("ivan", 6)
print(d)
