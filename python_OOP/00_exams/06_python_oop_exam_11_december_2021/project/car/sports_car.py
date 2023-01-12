from project.car.car import Car


class SportsCar(Car):
    SPEED_LIMIT = range(400, 600 + 1)

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)
