class Player:
    players_created = []

    def __init__(self, name, age, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")

        if value in Player.players_created:
            raise Exception(f"Name {value} is already used!")

        self.players_created.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value > 100 or value < 0:
            raise ValueError("Stamina not valid!")

        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.__stamina < 100

    def __str__(self):

        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

# first = Player("Ivan", 10)
# second = Player("Ivan", 20)
#
# print(Player.players_created[0].name)
