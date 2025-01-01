"""
Program to simulate the Monty Hall Game
"""

import random

doors = [0] * 3
goat_door = []

car_index = random.randint(0, 2)  # xth door will contain the car
doors[car_index] = "BMW"
for idx in range(3):
    if idx == car_index:
        continue
    else:
        doors[idx] = "Goat"
        goat_door.append(idx)

choice = int(input("Enter your choice: "))
door_open = random.choice(goat_door)  # Open a door that has a goat behind it
while door_open == choice:
    # Door opened shouldn't be the one that the player chose
    # Generate a goat door that is different from the one that the player chose
    door_open = random.choice(goat_door)
print(f"Door opened: {door_open}, has a goat")

swap_choice = input("Do you want to swap? (y/n): ")
if swap_choice == "y":
    if doors[choice] == "Goat":
        print("Player wins")
    else:
        print("Player lost")
else:
    if doors[choice] == "Goat":
        print("Player lost")
    else:
        print("Player wins")
