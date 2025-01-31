from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

function_on_menu = Menu()
coffee_machine = CoffeeMaker()
moneyMachine = MoneyMachine()

is_machine_on = True
while is_machine_on:
    options = function_on_menu.get_items()
    coffee_name = input(f"What would you like? {options} ").lower()
    if coffee_name == 'report':
        coffee_machine.report()
        moneyMachine.report()
    elif coffee_name in options:
        item_on_menu = function_on_menu.find_drink(coffee_name)
        # The item_on_menu is an object called MenuItem
        if coffee_machine.is_resource_sufficient(item_on_menu):
            if moneyMachine.make_payment(item_on_menu.cost):
                coffee_machine.make_coffee(item_on_menu)
    elif coffee_name == 'off':
        is_machine_on = False
    else:
        print("Invalid input. Pls check your spelling or input!")


