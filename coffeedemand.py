class CoffeeDemand:
    def __init__(self):
        self.demand = {
            "Espresso": 500,
            "Americano": 200,
            "Filter": 300,
            "Macchiato": 400,
            "Flat White": 600,
            "Latte": 1000
        }

    def get_demand(self, coffee_type):
        return self.demand.get(coffee_type)
