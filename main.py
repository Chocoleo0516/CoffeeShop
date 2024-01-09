from coffeeshop import CoffeeShop
from coffeedemand import CoffeeDemand


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer:")

def main():
    shop = CoffeeShop() #Create CoffeeShop instance
    get_month = get_integer_input("Please enter the number of months:")
    coffee_demand = CoffeeDemand()

    #start loop
    for month in range(1, get_month+1):
        print(f"=======Simulate{month}month=======:")

        #change number of barista
        barista_change = get_integer_input("Enter the change in the number of baristas (positive numbers increase, negative numbers decrease, 0 has no change):")
        while (len(shop.barista) + barista_change) < 1:
            barista_change = get_integer_input("At least one barista is required, please re-enter:")
        for n in range(1, abs(barista_change)+1):
            if barista_change > 0:
                name = input(f"number{n}barista is :")
                while True:
                    specialty = input('The specialty is (please choose among Espresso, Americano, Filter, Macchiato, Flat White, Latte, pay attention to the case. If there is no specialty, please enter 0)：')
                    # Check if the input is correct
                    if specialty in shop.ingredient.coffee_recipes or specialty == '0':
                        break
                    else:
                        print("The expertise entered is incorrect, please re-enter:")
                if specialty == "0" :
                    specialty = None
                shop.add_barista(name, specialty)
            if barista_change < 0:
                name = input(f"number{n}barista is:")
                shop.remove_barista(name)

        #update labour
        shop.update_labor() 

        #sellingcoffee
        for coffee_type in shop.ingredient.coffee_recipes:
            demand = coffee_demand.get_demand(coffee_type)
            print(f"{coffee_type}, demand:{demand}")
            sell = get_integer_input(f"how many{coffee_type}do you sell:") #quantity
            while sell > demand:
                    sell = get_integer_input(f"The sales quantity {sell} is greater than the demand {demand}, please re-enter。")

            #Determine whether the supply of raw materials and labor are sufficient. If sufficient, the funds will change.
            while True:
                if shop.is_labor_sufficient(coffee_type, sell):
                    if shop.sell_coffee(coffee_type, sell):
                         break  #If the raw materials and labor are sufficient, jump out of the loop                       
                    else:
                        production = shop.calculate_production(coffee_type)
                        sell = get_integer_input(f"Insufficient raw materials, please re-enter (capacity is:{production}):")
                else:
                    production = shop.calculate_production(coffee_type)
                    sell = get_integer_input(f"Insufficient labor force, please re-enter (capacity is: {production})：")

            shop.update_inventory(coffee_type, sell)    #Update inventory based on coffee type and quantity
        
        shop.cash -= (shop.cash_spend() + shop.storage_cost()) 

        shop.current()  #Show the status of the store before replenishing raw materials

        shop.inventory_depreciation()   #Calculate depreciation
    
        shop.buy_ingredient()   #Fill up warehouse and update cash
        if shop.cash < 0:
            print("bankrupted!")
            break

if __name__ == "__main__":
    main()











        

