from barista import Barista
from coffeeshop import CoffeeShop
from ingredient import Ingredient
from coffeedemand import CoffeeDemand  # 导入新增的 CoffeeDemand 类

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("请输入有效的整数。")

def main():
    shop = CoffeeShop() #创建CoffeeShop实例
    get_month = get_integer_input("请输入月数：")

    #开始循环
    for month in range(1, month+1):
        print(f"=======模拟第{month}个月=======:")

        #改变咖啡师人数
        barista_change = get_integer_input("输入咖啡师人数变化（正数增加，负数减少，0无变化）：")
        for n in range(1, abs(barista_change)+1):
            if barista_change > 0:
                name = get_integer_input(f"添加的第{n}个咖啡师名字是：")
                shop.add_barista(name)
            if barista_change < 0:
                name = get_integer_input(f"删除的第{n}个咖啡师名字是：")
                shop.remove_barista(name)
            
    #销售咖啡
    for coffee_type in shop.ingredients.coffee_recipes:
        demand = coffee_demand.get_demand(coffee_type)
        print(f"{coffee_type}，需求量：{demand}")
        sell = get_integer_input(f"{coffee_type}卖多少：")
        #判断原料供应量
        

