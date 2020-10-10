from Gym.project.customer import Customer
from Gym.project.equipment import Equipment
from Gym.project.exercise_plan import ExercisePlan
from Gym.project.subscription import Subscription
from Gym.project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id:int):
        subscription = [sub for sub in self.subscriptions if sub.id == subscription_id][0]
        customer = [cus for cus in self.customers if cus.id == subscription.customer_id][0]
        trainer = [trainer for trainer in self.trainers if trainer.id == subscription.trainer_id][0]
        plan = [plan for plan in self.plans if plan.trainer_id == trainer.id][0]
        equipment = [eq for eq in self.equipment if eq.id == plan.equipment_id][0]
        result = repr(subscription) + '\n'
        result += repr(customer) + '\n'
        result += repr(trainer) + '\n'
        result += repr(equipment) + '\n'
        result += repr(plan)
        return result

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
customer2 = Customer("George", "Hudson Court", "george.ball@gmail.com")
equipment = Equipment("Treadmill")
equipment2 = Equipment("Some Equipment")
trainer = Trainer("Peter")
trainer2 = Trainer("Sofronii")
subscription = Subscription("14.05.2020", 1, 1, 1)
subscription2 = Subscription("15.07.2019", 2, 1, 2)
plan = ExercisePlan(1, 1, 20)
plan2 = ExercisePlan.from_hours(1, 2, 3 )

gym = Gym()

gym.add_customer(customer)
gym.add_customer(customer2)
gym.add_equipment(equipment)
gym.add_equipment(equipment2)
gym.add_trainer(trainer)
gym.add_trainer(trainer2)
gym.add_plan(plan)
gym.add_plan(plan2)
gym.add_subscription(subscription)
gym.add_subscription(subscription2)

print(customer)
print(customer2)
print(equipment)
print(equipment2)
print(trainer)
print(trainer2)
print(plan)
print(plan2)
print(subscription)
print(subscription2)
print()
print(customer.autoincremented)
print(equipment.autoincremented)
print(trainer.autoincremented)
print(plan.autoincremented)
print(subscription.autoincremented)
print(gym.subscription_info(2))
