"""
Statistical simulation of a lottery game
"""

import random
import matplotlib.pyplot as plt

account = 0
x_values = []
y_values = []
for idx in range(20):
    x_values.append(idx + 1)
    bet = random.randint(1, 5)
    lucky_draw = random.randint(1, 5)
    if bet == lucky_draw:
        account = account + 900 - 100
    else:
        account = account - 100
    y_values.append(account)

print(f"Account balance: {account}")
plt.plot(x_values, y_values, "go-")
plt.title("Account balance over time")
plt.xlabel("Days")
plt.xticks(x_values)
plt.ylabel("Account balance")
plt.show()
