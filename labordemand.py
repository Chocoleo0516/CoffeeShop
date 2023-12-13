class Labordemand:
    def __init__(self):
        self.demand = {"Espresso": 3,
            "Americano": 2,
            "Filter": 1,
            "Macchiato": 4,
            "Flat White": 5,
            "Latte": 6
        }
    
    def get_demand(self, coffee_type):
        return self.demand.get(coffee_type)