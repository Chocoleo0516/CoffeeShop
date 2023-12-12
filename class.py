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

    def get_ingredients(self, coffee_type):
        # 返回指定咖啡类型所需的原料量
        return self.coffee_recipes.get(coffee_type, {})


class CoffeeShop:       #缺少错误处理
    def __init__(self, name):
        self.cash = 10000   #初始现金
        self.barista = []   #初始员工为空
        self.rent = 1500    #每月租金
        self.inventory = {"milk": 300, "beans": 20000, "spices": 4000}   #创建一个字典来储存初始原料
        self.prices = {
            "Espresso": 1.5,
            "Americano": 1.0,
            "Filter": 0.8,
            "Macchiato": 2.5,
            "Flat White": 2.2,
            "Latte": 2.0
        }   #创建字典储存咖啡售价
        self.ingredients = Ingredient()    #创建Ingredirnt实例

    def storage_cost(self):
        milk_cost = self.inventory.get("milk") * 0.10
        beans_cost = self.inventory.get("beans") * 0.001
        spices_cost = self.inventory.get("spices") * 0.001
        return milk_cost + beans_cost + spices_cost

    def add_barista(self, barista_name):
        #添加咖啡师
        if barista_name in self.barista:
            print(f"咖啡师 {barista_name} 已经存在于员工名单中。")
        else:
            self.barista.append(barista_name)
            print(f"咖啡师 {barista_name} 已添加到员工名单。")

    def remove_barista(self, barista_name):
        #移除咖啡师
        if barista_name in self.barista:
            self.barista.remove(barista_name)
        else:
            print(f"咖啡师 {barista_name} 不存在于员工名单中。")

    def cash_spend(self):
        #这里只包含工资与租金，不包含购买原料的价格
        wage = len(self.barista)*15*120
        return wage + self.rent
    
    def sell_coffee(self, coffee_type, quantity):
        #检查是否有足够的原料
        for ingredient, amount_per_unit in self.ingredients.recipes[coffee_type].items():
            if self.inventory.get(ingredient) < amount_per_unit * quantity:
                print(f"原料不足，无法制作 {quantity} 杯 {coffee_type}")
                return False

        #计算收入并更新现金
        price_per_cup = self.prices.get(coffee_type)
        income = quantity * price_per_cup
        self.cash += income
        print(f"成功销售 {quantity} 杯 {coffee_type}，收入 {income}")

        return True

    
    def update_inventory(self, coffee_type, quantity):
        #根据咖啡类型和数量更新库存
        #缺少库存小于0的警告
        recipe = self.ingredients.get_ingredients(coffee_type)
        if recipe:
            for ingredient, amount_per_unit in recipe.items():
                if ingredient in self.inventory:
                    self.inventory[ingredient] -= amount_per_unit * quantity
        else:
            print(f"未知的咖啡类型: {coffee_type}")
    
    def current(self):
        #显示咖啡店的当前状态
        print(f"Cash surplus: {self.cash}")  #打印剩余现金
        print("Inventory:", self.inventory) #打印库存      
        print("Baristas:")  #打印咖啡师名字
        for b in self.barista:
            print(b)

