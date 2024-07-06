from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)




# Object Oriented Programing(OOP)
# 模擬角色需思考(if waiter )，
    # attribute (變數) :擁有甚麼(has)
        # is_holding_plate = True
        # table_responsible = [4,5,6]
    # methon (function) : 該做甚麼(does)
        # def take_order(table,order): #takes order to chef
        # def take_payment(amount): add the money to restaurant

# 一個class(waiter)，可以有多個對象(Object)
    # 創建一個waiter，但裡面可以有兩種對象（henry betty）


# class =藍圖， object = 實際產生運用的項目


# code的形式
    # car = CarBlueprint()
    #car(Object)是由CarBlueprint(class(首字母大寫))這個藍圖產生的

    # car.speed (在car(object)中拿speed(attribute)這個變數

    # car.stop() (在car(object)中拿stop()(methon)這個function

# Turtle graphics

    # from turtle import Turtle, Screen
    # timmy = Turtle()
    # print(timmy)
    # timmy.shape("turtle")
    # #變形狀成烏龜
    # timmy.color("purple2")
    # #改顏色
    # timmy.fd(100)
    # #往前移動
    #
    # my_screen = Screen()
    # print(my_screen.canvheight)
    # my_screen.exitonclick()


# Python packages(https://pypi.org/)
    # from prettytable import PrettyTable
    # table = PrettyTable()
    # table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
    # table.add_column("Type",["Electric","Water","Fire"])
    # table.align = "l"
    # # 將表格從至中改為靠左
    #
    # print(table)

