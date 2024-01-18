"""
Prints the reward in the current level and cumulative reward at each level
Logic:
Each level reward is decided by the product of level number sqaured and 50 (50 * level * level)
So cumulative reward becomes sum of squares of natural numbers till the level multiplied by 50
"""

completed_level = int(input("Enter level: "))
cumulative_reward = 0
for level in range(1, completed_level + 1):
    print(f"Level {str(level)}")
    reward = 50 * level * level
    cumulative_reward += reward
    print(f"Current level reward: {reward} \t Cumulative reward: {cumulative_reward}")
