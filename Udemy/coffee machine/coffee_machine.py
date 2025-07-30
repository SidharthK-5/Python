from resources import MENU, resources

resources = resources.copy()
balance = 0


def is_resource_sufficient(product: str) -> bool:
    resources_required = MENU[product]["ingredients"]
    resources_sufficient = True
    insufficient_resources = []

    # Check if each resource is in enough quantity for the product
    for key in resources_required.keys():
        if resources_required[key] > resources[key]:
            insufficient_resources.append(key)
            resources_sufficient = False

    if insufficient_resources:
        # Print the insufficient recourses if there are
        print(f"Sorry, there is not enough {', '.join(insufficient_resources)}")

    return resources_sufficient


def process_inserted_coins(quarters: int, dimes: int, nickels: int, pennies: int):
    return quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01


def is_transaction_successful(actual_cost: float, user_amount: float) -> bool:
    if actual_cost > user_amount:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif actual_cost == user_amount:
        return True
    else:
        print(f"“Here is ${round(user_amount - actual_cost, 2)} dollars in change.")
        return True


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        break
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${balance}")
    elif user_input in ("espresso", "latte", "cappuccino"):
        # Check if there are enough resources to make the product
        if is_resource_sufficient(product=user_input):
            print("Please insert coins.")
            quarter_coins = int(input("how many quarters?: "))
            dime_coins = int(input("how many dimes?: "))
            nickel_coins = int(input("how many nickles?: "))
            pennie_coins = int(input("how many pennies?: "))

            inserted_sum = process_inserted_coins(
                quarters=quarter_coins,
                dimes=dime_coins,
                nickels=nickel_coins,
                pennies=pennie_coins,
            )
            product_cost = MENU[user_input]["cost"]
            if is_transaction_successful(
                actual_cost=product_cost, user_amount=inserted_sum
            ):
                # Update balance and make coffee (reduce resource amount)
                balance += product_cost
                resources_consumed = MENU[user_input]["ingredients"]
                resources["water"] -= resources_consumed["water"]
                resources["milk"] -= resources_consumed.get("milk", 0)
                resources["coffee"] -= resources_consumed["coffee"]
                print(f"Here is your {user_input}. Enjoy!")
    else:
        print("Wrong input!!! Try again...")
