class Ingredient:
    def __init__(self):
        # 定义每种咖啡所需原料的单位消耗量
        self.coffee_recipes = {
            "Espresso": {"beans": 8},
            "Americano": {"beans": 6},
            "Filter": {"beans": 4},
            "Macchiato": {"milk": 100, "beans": 8, "spices": 2},
            "Flat White": {"milk": 200, "beans": 8, "spices": 1},
            "Latte": {"milk": 300, "beans": 8, "spices": 3}
        }

    def get_ingredient(self, coffee_type):
        # 返回指定咖啡类型所需的原料量
        return self.coffee_recipes[coffee_type]