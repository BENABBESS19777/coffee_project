from os import waitstatus_to_exitcode

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
Money = 0
water_stock = resources['water']
milk_stock = resources['milk']
coffee_stock = resources['coffee']

#ALL FUNCTIONS#
def add_coins_inserted ():
    """ Calculate the monetary value of the coins inserted """
    return quarters_numbers * 0.25 + dimes_numbers * 0.1 + nickles_numbers * 0.05 + pennies_numbers * 0.01
def change_coins_inserted():
    return monetary_value_inserted - 1.5


# print start program
user_choice = input("What would you like? (Espresso/ Latte/ Cappucino) :")
print(user_choice)
if user_choice == 'report':
    for key, value in resources.items():
        print(f"{key} : {value}")
    print(f"Money : {Money}")
elif user_choice == 'Espresso':
    print("please insert coins.")
    quarters_numbers = int(input("How many quarters? : "))
    dimes_numbers = int(input("How many dimes? : "))
    nickles_numbers = int( input("How many nickles? : "))
    pennies_numbers = int(input("How many quarters? : "))
    monetary_value_inserted = add_coins_inserted()
    if monetary_value_inserted == 1.5 :
        print("Here is your Espresso ,Enjoy !")
        water_stock-= 50
        milk_stock -= 0
        coffee_stock -= 18
    elif monetary_value_inserted > 1.5 :
        print(f"Here is {change_coins_inserted()} in change ")
        print("Here is your Espresso ,Enjoy !")
        water_stock -= 50
        milk_stock -= 0
        coffee_stock -= 18
    else:
        print("Sorry that's not enough money, Money refunded")
print(water_stock)