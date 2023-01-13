class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price > self.__budget:
            return "Not enough budget"

        if len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, name):
        try:
            searched_worker = [x for x in self.workers if x.name == name][0]
            self.workers.remove(searched_worker)
            return f"{name} fired successfully"
        except IndexError:
            return f"There is no {name} in the zoo"

    def pay_workers(self):
        all_workers_salaries = sum([x.salary for x in self.workers])

        if self.__budget < all_workers_salaries:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= all_workers_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        all_animals_money_for_care = sum([x.money_for_care for x in self.animals])

        if self.__budget < all_animals_money_for_care:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= all_animals_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    @staticmethod
    def elements_sorter(collection, first_el, second_el, third_el):
        dct = {first_el: [], second_el: [], third_el: []}

        for el in collection:
            dct[type(el).__name__].append(repr(el))
        return dct

    def animals_status(self):
        res = [f"You have {len(self.animals)} animals"]
        dct = self.elements_sorter(self.animals, "Lion", "Tiger", "Cheetah")

        for animal, lst in dct.items():
            res.append(f"----- {len(lst)} {animal}s:")
            res.extend(lst)

        return '\n'.join(res)

    def workers_status(self):
        res = [f"You have {len(self.workers)} workers"]
        dct = self.elements_sorter(self.workers, "Keeper", "Caretaker", "Vet")

        for worker, lst in dct.items():
            res.append(f"----- {len(lst)} {worker}s:")
            res.extend(lst)

        return '\n'.join(res)