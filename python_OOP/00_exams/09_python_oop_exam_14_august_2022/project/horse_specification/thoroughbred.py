from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    maximum_speed = 140

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + 3 >= self.maximum_speed:
            self.speed = self.maximum_speed
        else:
            self.speed += 3
