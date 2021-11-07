from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    is_on = True

    coffee_machine = CoffeeMaker()
    simple_menu = Menu()
    money_machine = MoneyMachine()


    options = simple_menu.get_items()
    
    while is_on:
        choice = input(f"Please choose what to drink {options}\n")
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_machine.report()
            money_machine.report()
        else:
            drink = simple_menu.find_drink(choice)
            if coffee_machine.is_resource_sufficient(drink)and money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
        

if __name__ == '__main__':
    main()