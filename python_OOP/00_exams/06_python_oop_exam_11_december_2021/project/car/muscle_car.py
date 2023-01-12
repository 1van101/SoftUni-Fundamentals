from project.car.car import Car


class MuscleCar(Car):
    SPEED_LIMIT = range(250, 450 + 1)

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

