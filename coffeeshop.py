from ingredient import Ingredient  # 导入Ingredient类
from barista import Barista #导入Barista类
from labordemand import Labordemand

class CoffeeShop:       #缺少错误处理
    def __init__(self):
        self.cash = 10000   #初始现金
        self.rent = 1500    #每月租金
        self.inventory = {"milk": 300000, "beans": 20000, "spices": 4000}   #创建一个字典来储存初始原料
        self.prices = {
            "Espresso": 1.5,
            "Americano": 2.5,
            "Filter": 1.5,
            "Macchiato": 3.0,
            "Flat White": 3.5,
            "Latte": 4.0
        }   #创建字典储存咖啡售价
        self.ingredient = Ingredient()    #创建Ingredirnt实例
        self.barista = []  #储存Barista实例
        self.labordemand = Labordemand()
        #self.labor = len(self.barista) * 80 * 60    #初始的计算每月劳动力总量(minutes)
        self.labor = {"general": 0, "Espresso": 0, "Americano": 0, "Filter": 0, "Macchiato": 0, "Flat White": 0, "Latte": 0}

    def storage_cost(self):
        #计算原料储存费用
        milk_cost = self.inventory["milk"] * 0.0001
        beans_cost = self.inventory["beans"] * 0.001
        spices_cost = self.inventory["spices"] * 0.001
        return milk_cost + beans_cost + spices_cost

    # def update_labor(self):
    #     #初始的更新劳动力
    #     self.labor = len(self.barista) * 80 * 60

    def update_labor(self): #更新劳动力
        #重置劳动力
        for coffee in self.labor:
            self.labor[coffee] = 0
        #根据专长更新劳动力
        for barista in self.barista:
            specialty = barista.get_specialty()
            if specialty:
                self.labor[specialty] += 80*60
            else:
                self.labor["general"] += 80 * 60


    def add_barista(self, barista_name, specialty = None):
        #添加咖啡师
        #检查咖啡师名字是否已经存在
        for barista in self.barista:
            if barista.get_name() == barista_name:
                print(f"咖啡师 {barista_name} 已存在，请输入不同的名字。")
                return  #提前结束方法
        new_barista = Barista(barista_name, specialty)
        self.barista.append(new_barista)
        # self.update_labor()  #更新劳动力
        print(f"咖啡师 {barista_name} 已添加到员工名单。")

    def remove_barista(self, barista_name):
        #移除咖啡师
        for barista in self.barista:
            if barista.get_name() == barista_name:
                self.barista.remove(barista)
                print(f"咖啡师 {barista_name} 被移除。")
                # self.update_labor()  #更新劳动力
                break
        else:   #循环正常结束时执行
            print(f"咖啡师 {barista_name} 不存在于员工名单中。")

    def cash_spend(self):
        #不包含购买原料的花销
        wage = len(self.barista)*15*120
        return wage + self.rent

    # def is_labor_sufficient(self, coffee_type, quantity):
    #     #初始的检查是否有足够的劳动力
    #     required_labor = quantity * self.labordemand.get_demand(coffee_type)
    #     return self.labor >= required_labor

    def is_labor_sufficient(self, coffee_type, quantity):   #检查是否有足够的劳动力
        required_labor = quantity * self.labordemand.get_demand(coffee_type)
        available_labor = self.labor["general"] + (self.labor[coffee_type] * 2)
        return available_labor >= required_labor

    def sell_coffee(self, coffee_type, quantity):
        #检查是否有足够的原料
        for ingredient, amount_per_unit in self.ingredient.coffee_recipes[coffee_type].items():
            if self.inventory[ingredient] < amount_per_unit * quantity:
                print(f"原料不足，无法制作 {quantity} 杯 {coffee_type}")
                return False

        #计算收入并更新现金
        price_per_cup = self.prices[coffee_type]
        income = quantity * price_per_cup
        self.cash += income
        print(f"成功销售 {quantity} 杯 {coffee_type}，收入 {income}")
        # self.labor -= quantity * self.labordemand.get_demand(coffee_type) #初始更新劳动力
        #更新劳动力
        required_labor = quantity * self.labordemand.get_demand(coffee_type)
        if self.labor[coffee_type] >= (required_labor/2):
            self.labor[coffee_type] -= (required_labor/2)
        else:
            self.labor["general"] -= (required_labor - self.labor[coffee_type]*2)
            self.labor[coffee_type] = 0
        return True

    def calculate_production(self, coffee_type):
        # 计算基于劳动力的最大产量
        max_labor = (self.labor["general"] + (self.labor[coffee_type] * 2)) // self.labordemand.get_demand(coffee_type)

        # 计算基于原料的最大产量
        ingredient = self.ingredient.get_ingredient(coffee_type)
        max_ingredients = min(self.inventory[ingredient] // amount for ingredient, amount in ingredient.items())

        # 返回两者中的最小值
        return min(max_labor, max_ingredients)

    def inventory_depreciation(self):
        #计算折旧
        self.inventory["milk"] *= 0.6
        self.inventory["beans"] *= 0.9

    def update_inventory(self, coffee_type, quantity):
        #根据咖啡类型和数量更新库存
        recipe = self.ingredient.get_ingredient(coffee_type)
        if recipe:
            for ingredient, amount_per_unit in recipe.items():
                if ingredient in self.inventory:
                    self.inventory[ingredient] -= amount_per_unit * quantity
        else:
            print(f"未知的咖啡类型: {coffee_type}")

    def buy_ingredient(self):
        #购买原材料并加满仓库，更新现金
        buy_milk = (300000 - self.inventory["milk"]) * 0.0003
        buy_beans = (20000 - self.inventory["beans"]) * 0.1
        buy_spices = (4000- self.inventory ["spices"]) * 0.05
        self.inventory = {"milk": 300000, "beans": 20000, "spices": 4000}   #加满仓库
        self.cash -= (buy_milk + buy_beans + buy_spices)
    
    def current(self):
        #显示咖啡店的当前状态
        print(f"Cash surplus: {self.cash}")  #打印剩余现金
        print("Inventory:", self.inventory) #打印库存 
        for barista in self.barista:
            name = barista.get_name()
            specialty = barista.get_specialty() if barista.get_specialty() else "无专长"
            print(f"咖啡师 {name}，专长：{specialty}")     


