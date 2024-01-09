from ingredient import Ingredient  
from barista import Barista
from labordemand import Labordemand

class CoffeeShop:       
    def __init__(self):
        self.cash = 10000   #Initial cash
        self.rent = 1500    #Monthly rent
        self.inventory = {"milk": 300000, "beans": 20000, "spices": 4000}   #creat a dictionary to store inventory
        self.prices = {
            "Espresso": 1.5,
            "Americano": 2.5,
            "Filter": 1.5,
            "Macchiato": 3.0,
            "Flat White": 3.5,
            "Latte": 4.0
        }   #Create a dictionary to store coffee selling prices
        self.ingredient = Ingredient()    #Creating an instance of Ingredirnt
        self.barista = []  #Store Barista instances
        self.labordemand = Labordemand()
        #self.labor = len(self.barista) * 80 * 60    #Initial calculation of total monthly labour force(minutes)
        self.labor = {"general": 0, "Espresso": 0, "Americano": 0, "Filter": 0, "Macchiato": 0, "Flat White": 0, "Latte": 0}

    def storage_cost(self):
        #Calculation of raw material storage costs
        milk_cost = self.inventory["milk"] * 0.0001
        beans_cost = self.inventory["beans"] * 0.001
        spices_cost = self.inventory["spices"] * 0.001
        return milk_cost + beans_cost + spices_cost

    # def update_labor(self):
    #     #Initially update labour force
    #     self.labor = len(self.barista) * 80 * 60

    def update_labor(self): #Updating the labour force
        #reset the labour force
        for coffee in self.labor:
            self.labor[coffee] = 0
        #update labour by specialty
        for barista in self.barista:
            specialty = barista.get_specialty()
            if specialty:
                self.labor[specialty] += 80*60
            else:
                self.labor["general"] += 80 * 60


    def add_barista(self, barista_name, specialty = None):
        #add barista
        #check if existence
        for barista in self.barista:
            if barista.get_name() == barista_name:
                input(f"barista {barista_name} already existing, Please retype.")
                return  
        new_barista = Barista(barista_name, specialty)
        self.barista.append(new_barista)
        # self.update_labor()  #update labour
        print(f"barista {barista_name} Added to staff list.")

    def remove_barista(self, barista_name):
        #Remove barista
        for barista in self.barista:
            if barista.get_name() == barista_name:
                self.barista.remove(barista)
                print(f"barista {barista_name} removed.")
                # self.update_labor()  #update labour
                break
        else:   #Executed when the loop ends normally
            input(f"barista {barista_name} Does not exist in employee list.")

    def cash_spend(self):
        #Does not include the cost of purchasing raw materials
        wage = len(self.barista)*15*120
        return wage + self.rent

    # def is_labor_sufficient(self, coffee_type, quantity):
    #     #Initial check to see if there is enough labor
    #     required_labor = quantity * self.labordemand.get_demand(coffee_type)
    #     return self.labor >= required_labor

    def is_labor_sufficient(self, coffee_type, quantity):   #Check if there is enough labor
        required_labor = quantity * self.labordemand.get_demand(coffee_type)
        available_labor = self.labor["general"] + (self.labor[coffee_type] * 2)
        return available_labor >= required_labor

    def sell_coffee(self, coffee_type, quantity):
        #Check if there are enough ingredients
        for ingredient, amount_per_unit in self.ingredient.coffee_recipes[coffee_type].items():
            if self.inventory[ingredient] < amount_per_unit * quantity:
                print(f"Insufficient ingredient to make {quantity} cuos of  {coffee_type}")
                return False

        #Calculate income and update cash
        price_per_cup = self.prices[coffee_type]
        income = quantity * price_per_cup
        self.cash += income
        print(f"successful sale {quantity} cup of  {coffee_type}, income {income}")
        # self.labor -= quantity * self.labordemand.get_demand(coffee_type) #Initial Update Workforce
        #updateworkforce
        required_labor = quantity * self.labordemand.get_demand(coffee_type)
        if self.labor[coffee_type] >= (required_labor/2):
            self.labor[coffee_type] -= (required_labor/2)
        else:
            self.labor["general"] -= (required_labor - self.labor[coffee_type]*2)
            self.labor[coffee_type] = 0
        return True

    def calculate_production(self, coffee_type):
        #Calculate the maximum output based on labor
        max_labor = (self.labor["general"] + (self.labor[coffee_type] * 2)) // self.labordemand.get_demand(coffee_type)

        # Calculate the maximum output based on raw materials
        ingredient = self.ingredient.get_ingredient(coffee_type)
        max_ingredients = min(self.inventory[ingredient] // amount for ingredient, amount in ingredient.items())

        #Returns the minimum of the two
        return min(max_labor, max_ingredients)

    def inventory_depreciation(self):
        #Calculate depreciation
        self.inventory["milk"] *= 0.6
        self.inventory["beans"] *= 0.9

    def update_inventory(self, coffee_type, quantity):
        #Update inventory based on coffee type and quantity
        recipe = self.ingredient.get_ingredient(coffee_type)
        if recipe:
            for ingredient, amount_per_unit in recipe.items():
                if ingredient in self.inventory:
                    self.inventory[ingredient] -= amount_per_unit * quantity
        else:
            print(f"未知的咖啡类型: {coffee_type}")

    def buy_ingredient(self):
        #Buy raw materials and fill up the warehouse, update cash
        buy_milk = (300000 - self.inventory["milk"]) * 0.0003
        buy_beans = (20000 - self.inventory["beans"]) * 0.1
        buy_spices = (4000- self.inventory ["spices"]) * 0.05
        self.inventory = {"milk": 300000, "beans": 20000, "spices": 4000}   #加满仓库
        self.cash -= (buy_milk + buy_beans + buy_spices)
    
    def current(self):
        #Display the current status of the coffee shop
        print(f"Cash surplus: {self.cash}")  #print remaining cash
        print("Inventory:", self.inventory) #printstock 
        for barista in self.barista:
            name = barista.get_name()
            specialty = barista.get_specialty() if barista.get_specialty() else "no specialty"
            print(f"barista {name}，specialty：{specialty}")     


