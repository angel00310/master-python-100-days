MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# 2.投幣的費用

def paid_money():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total

# 3.確認價格是否一致
def is_money_paid(paid_money,coffee_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if paid_money >= coffee_cost:
        change = round(paid_money - coffee_cost, 2)
        # 為了使用全區參數，用global帶入區域
        global profit
        profit += coffee_cost
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# 4.確認資源是否足夠
def is_resource_enough(order_coffee):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_coffee:
        if order_coffee[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True

# 5.完成咖啡減資源
def make_coffee(coffee,order_resource):
    """Deduct the required ingredients from the resources."""
    for item in order_resource:
        resources[item] -= order_resource[item]
    print(f"Here is your {coffee} ☕️. Enjoy!")


# 6.買咖啡
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Water: {resources['water']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_enough(drink["ingredients"]):
            payment = paid_money()
            if is_money_paid(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])
