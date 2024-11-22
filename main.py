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
#VARIABLES

Money = 0
#stock

water_stock = resources['water']
milk_stock = resources['milk']
coffee_stock = resources['coffee']

#espresso description

water_espresso = MENU['espresso']["ingredients"]["water"]
coffee_espresso = MENU['espresso']["ingredients"]["coffee"]
cost_espresso = MENU['espresso']["cost"]
#latte description

water_latte = MENU['latte']["ingredients"]["water"]
milk_latte = MENU['latte']["ingredients"]["milk"]
coffee_latte = MENU['latte']["ingredients"]["coffee"]
cost_latte = MENU['latte']["cost"]
#cappuccino description

water_cappuccino = MENU['cappuccino']["ingredients"]["water"]
milk_cappuccino = MENU['cappuccino']["ingredients"]["milk"]
coffee_cappuccino = MENU['cappuccino']["ingredients"]["coffee"]
cost_cappuccino = MENU['cappuccino']["cost"]

#ALL FUNCTIONS

def add_coins_inserted ():
    """ Calculate the monetary value of the coins inserted """
    return quarters_numbers * 0.25 + dimes_numbers * 0.1 + nickles_numbers * 0.05 + pennies_numbers * 0.01
def change_coins_inserted():
    """Return money in change"""
    return monetary_value_inserted - 1.5
def print_report():
    """Shows the current resources values"""
    print(f"water : {water_stock} ml")
    print(f"milk : {milk_stock} ml")
    print(f"coffee : {coffee_stock} g")
    print(f"Money : {Money} $")
def coffee_choice(coffee):
    pass



# print start program
user_choice = input("What would you like? (espresso/ latte/ cappuccino) :")
print(user_choice)
#Report
if user_choice == 'report':
    print_report()
#Espresso
elif user_choice == 'Espresso':
    print("please insert coins.")
    quarters_numbers = int(input("How many quarters? : "))
    dimes_numbers = int(input("How many dimes? : "))
    nickles_numbers = int( input("How many nickles? : "))
    pennies_numbers = int(input("How many quarters? : "))
    monetary_value_inserted = add_coins_inserted()
    if monetary_value_inserted == MENU['espresso']["cost"] :
        print("Here is your Espresso ,Enjoy !")
        water_stock-=  MENU['espresso']["ingredients"]["water"]
        milk_stock -= 0
        coffee_stock -= MENU['espresso']["ingredients"]["coffee"]
    elif monetary_value_inserted > MENU['espresso']["cost"] :
        print(f"Here is {change_coins_inserted()} in change ")
        print("Here is your Espresso ,Enjoy !")
        water_stock -= MENU['espresso']["ingredients"]["water"]
        milk_stock -= 0
        coffee_stock -= MENU['espresso']["ingredients"]["coffee"]
    else:
        print("Sorry that's not enough money, Money refunded")
#Latte
elif user_choice == 'latte':
    print("please insert coins.")
    quarters_numbers = int(input("How many quarters? : "))
    dimes_numbers = int(input("How many dimes? : "))
    nickles_numbers = int( input("How many nickles? : "))
    pennies_numbers = int(input("How many quarters? : "))
    monetary_value_inserted = add_coins_inserted()
    if monetary_value_inserted == MENU['latte']["cost"] :
        print("Here is your latte ,Enjoy !")
        water_stock-=  MENU['latte']["ingredients"]["water"]
        milk_stock -= 0
        coffee_stock -= MENU['latte']["ingredients"]["coffee"]
    elif monetary_value_inserted > MENU['latte']["cost"] :
        print(f"Here is {change_coins_inserted()} in change ")
        print("Here is your latte ,Enjoy !")
        water_stock -= MENU['latte']["ingredients"]["water"]
        milk_stock -= MENU['latte']["ingredients"]["milk"]
        coffee_stock -= MENU['latte']["ingredients"]["coffee"]
    else:
        print("Sorry that's not enough money, Money refunded")

#Cappucino
elif user_choice == 'cappuccino':
    print("please insert coins.")
    quarters_numbers = int(input("How many quarters? : "))
    dimes_numbers = int(input("How many dimes? : "))
    nickles_numbers = int( input("How many nickles? : "))
    pennies_numbers = int(input("How many quarters? : "))
    monetary_value_inserted = add_coins_inserted()
    if monetary_value_inserted == MENU['cappuccino']["cost"] :
        print("Here is your cappuccino ,Enjoy !")
        water_stock-=  MENU['cappuccino']["ingredients"]["water"]
        milk_stock -= MENU['cappuccino']["ingredients"]["milk"]
        coffee_stock -= MENU['cappuccino']["ingredients"]["coffee"]
    elif monetary_value_inserted > MENU['cappuccino']["cost"] :
        print(f"Here is {change_coins_inserted()} in change ")
        print("Here is your latte ,Enjoy !")
        water_stock -= MENU['cappuccino']["ingredients"]["water"]
        milk_stock -= 0
        coffee_stock -= MENU['cappuccino']["ingredients"]["coffee"]
    else:
        print("Sorry that's not enough money, Money refunded")