#from barista import Barista
from coffeeshop import CoffeeShop
#from ingredient import Ingredient
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
    coffee_demand = CoffeeDemand()

    #开始循环
    for month in range(1, get_month+1):
        print(f"=======模拟第{month}个月=======:")

        #改变咖啡师人数
        barista_change = get_integer_input("输入咖啡师人数变化（正数增加，负数减少，0无变化）：")
        for n in range(1, abs(barista_change)+1):
            if barista_change > 0:
                name = input(f"添加的第{n}个咖啡师名字是：")
                specialty = input('专长是(请在Espresso, Americano, Filter, Macchiato0, Flat White, Latte中选择，注意大小写。如果没有专长，请输入0)：')
                if specialty == "0" :
                    specialty = None
                shop.add_barista(name, specialty)
            if barista_change < 0:
                name = input(f"删除的第{n}个咖啡师名字是：")
                shop.remove_barista(name)

        #更新劳动力
        shop.update_labor()  #更新劳动力

        #销售咖啡
        for coffee_type in shop.ingredient.coffee_recipes:
            demand = coffee_demand.get_demand(coffee_type)
            print(f"{coffee_type}，需求量：{demand}")
            sell = get_integer_input(f"{coffee_type}卖多少：") #quantity
        
            #判断原料供应量与劳动力是否充足，如果充足则资金发生改变
            while True:
                if shop.is_labor_sufficient(coffee_type, sell):
                    if shop.sell_coffee(coffee_type, sell):
                         break  #如果原料和劳动力都足够，跳出循环                       
                    else:
                        sell = get_integer_input("原材料不足，请重新输入：")
                else:
                    sell = get_integer_input("劳动力不足，请重新输入：")

            shop.update_inventory(coffee_type, sell)    #根据咖啡类型和数量更新库存
        
        shop.cash -= (shop.cash_spend() + shop.storage_cost()) 

        shop.current()  #显示商店补充原料前的状态

        shop.inventory_depreciation()   #计算折旧
    
        shop.buy_ingredient()   #加满仓库并更新现金
        if shop.cash < 0:
            print("破产了！")
            break

if __name__ == "__main__":
    main()











        

