from customer import Customer
from equipment import Equipment
from exercise_plan import ExercisePlan
from subscription import Subscription
from trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.get_info(self.subscriptions, subscription_id)
        customer = self.get_info(self.customers, subscription_id)
        trainer = self.get_info(self.trainers, subscription_id)
        equipment = self.get_info(self.equipment, subscription_id)
        plan = self.get_info(self.plans, subscription_id)

        return f"{subscription}\n" \
               f"{customer}\n" \
               f"{trainer}\n" \
               f"{equipment}\n" \
               f"{plan}"

    @staticmethod
    def get_info(collection, id):
        return [x for x in collection if x.id == id][0]
