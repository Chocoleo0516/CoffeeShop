class Ingredient:
    def __init__(self):
        # Define the unit consumption of raw materials required for each coffee
        self.coffee_recipes = {
            "Espresso": {"beans": 8},
            "Americano": {"beans": 6},
            "Filter": {"beans": 4},
            "Macchiato": {"milk": 100, "beans": 8, "spices": 2},
            "Flat White": {"milk": 200, "beans": 8, "spices": 1},
            "Latte": {"milk": 300, "beans": 8, "spices": 3}
        }

    def get_ingredient(self, coffee_type):
        #Returns the amount of ingredients required for the specified coffee type
        return self.coffee_recipes[coffee_type]