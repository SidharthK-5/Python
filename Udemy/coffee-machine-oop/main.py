from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while True:
    user_input = input(f"What would you like to have? ({menu.get_items()}): ").lower()
    if user_input == "off":
        break
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if drink:
            if coffee_maker.is_resource_sufficient(
                drink=drink
            ) and money_machine.make_payment(cost=drink.cost):
                coffee_maker.make_coffee(order=drink)
