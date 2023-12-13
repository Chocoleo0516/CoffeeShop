from ingredient import Ingredient  # 导入 Ingredient 类
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
        self.labor = len(self.barista) * 80 * 60    #每月劳动力总量(minutes)

    def storage_cost(self):
        milk_cost = self.inventory.get("milk") * 0.10
        beans_cost = self.inventory.get("beans") * 0.001
        spices_cost = self.inventory.get("spices") * 0.001
        return milk_cost + beans_cost + spices_cost

    def update_labor(self):
        #更新劳动力
        self.labor = len(self.barista) * 80 * 60

    def add_barista(self, barista_name):
        #添加咖啡师
        #检查咖啡师名字是否已经存在
        for barista in self.barista:
            if barista.get_name() == barista_name:
                print(f"咖啡师 {barista_name} 已存在，请输入不同的名字。")
                return  #提前结束方法
        new_barista = Barista(barista_name)
        self.barista.append(new_barista)
        self.update_labor()  #更新劳动力
        print(f"咖啡师 {barista_name} 已添加到员工名单。")

    def remove_barista(self, barista_name):
        #移除咖啡师
        for barista in self.barista:
            if barista.get_name() == barista_name:
                self.barista.remove(barista)
                print(f"咖啡师 {barista_name} 被移除。")
                self.update_labor()  #更新劳动力
                break
        else:   #循环正常结束时执行
            print(f"咖啡师 {barista_name} 不存在于员工名单中。")

    def cash_spend(self):
        #这里只包含工资与租金，不包含购买原料的价格
        wage = len(self.barista)*15*120
        return wage + self.rent
    
    def is_labor_sufficient(self, coffee_type, quantity):
        #检查是否有足够的劳动力
        required_labor = quantity * self.labordemand.get_demand(coffee_type)
        return self.labor >= required_labor

    def sell_coffee(self, coffee_type, quantity):
        #检查是否有足够的原料
        for ingredient, amount_per_unit in self.ingredient.coffee_recipes[coffee_type].items():
            if self.inventory.get(ingredient) < amount_per_unit * quantity:
                print(f"原料不足，无法制作 {quantity} 杯 {coffee_type}")
                return False

        #计算收入并更新现金与劳动力
        price_per_cup = self.prices.get(coffee_type)
        income = quantity * price_per_cup
        self.cash += income
        print(f"成功销售 {quantity} 杯 {coffee_type}，收入 {income}")
        self.labor -= quantity * self.labordemand.get_demand(coffee_type)

        return True

    
    def update_inventory(self, coffee_type, quantity):
        #根据咖啡类型和数量更新库存
        recipe = self.ingredient.get_ingredient(coffee_type)
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
        print("Barista:")  #打印咖啡师名字
        for b in self.barista:
            print(b)

