import os

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


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_coins_inserted(quarters, dimes, nickles, pennies):
    """ Calculate the monetary value of the coins inserted """
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def change_coins_inserted(monetary_value_inserted, coffee_cost):
    """Return money in change"""
    return round(monetary_value_inserted - coffee_cost, 2)


def print_report():
    """Shows the current resources values"""
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${Money}")


def check_resources(coffee):
    """Check if there are enough resources to make the coffee"""
    for ingredient in MENU[coffee]["ingredients"]:
        if resources[ingredient] < MENU[coffee]["ingredients"][ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


Money = 0
make_coffee = True

while make_coffee:
    clear_terminal()
    user_choice = input(
        "What would you like? (espresso/ latte/ cappuccino) or type 'report' to see resources or 'off' to turn off: ").lower()

    if user_choice == 'report':
        print_report()
    elif user_choice == 'off':
        make_coffee = False
    elif user_choice in MENU:
        if check_resources(user_choice):
            print("Please insert coins.")
            quarters_numbers = int(input("How many quarters? : "))
            dimes_numbers = int(input("How many dimes? : "))
            nickles_numbers = int(input("How many nickles? : "))
            pennies_numbers = int(input("How many pennies? : "))

            monetary_value_inserted = add_coins_inserted(quarters_numbers, dimes_numbers, nickles_numbers,
                                                         pennies_numbers)
            coffee_cost = MENU[user_choice]["cost"]

            if monetary_value_inserted >= coffee_cost:
                change = change_coins_inserted(monetary_value_inserted, coffee_cost)
                Money += coffee_cost
                for ingredient in MENU[user_choice]["ingredients"]:
                    resources[ingredient] -= MENU[user_choice]["ingredients"][ingredient]
                print(f"Here is your {user_choice}, enjoy!")
                if change > 0:
                    print(f"Here is ${change} in change.")
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Invalid choice. Please try again.")