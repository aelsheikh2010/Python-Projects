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


def resource(resource_data):
    """print available resources with report"""
    available_water = resource_data["water"]
    available_milk = resource_data["milk"]
    available_coffee = resource_data["coffee"]
    return available_water, available_milk, available_coffee

def is_resources_sufficient(order_ingredients):
    """returns True when order can be made, return False if ingrediants are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Return total number of coins inserted"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def Check_transaction_successful(payment_money,drink_cost):
    """return true if payment is sufficient or false if payment is insufficient"""
    if payment_money >= drink_cost:
        change = round(payment_money - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """deduct the order ingredient from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here's your drink {drink_name} ☕")


should_continue = True

while should_continue:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        should_continue = False
    elif choice == "report":
       resource_variables = resource(resources)
       water,milk,coffee = resource_variables
       print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if Check_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])










