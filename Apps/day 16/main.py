from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
coins = MoneyMachine()
menu = Menu()
quitting = False

while quitting == False:
    print("What would you like?  (espresso/latte/cappuccino/):")
    resp = input()

    if resp == 'off':
        quitting = True

    elif resp == 'report':

        print(machine.report())
        print(coins.report())

    else:
        drink = menu.find_drink(resp)
        machine.is_resource_sufficient(drink)
        if machine.is_resource_sufficient(drink) == False:
            break

        coins.make_payment(drink.cost)
        if coins.make_payment(drink.cost) == True:
            machine.make_coffee(drink)
        else:
            break
