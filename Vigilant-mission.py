L = int(input("Enter level : "))
reward = 0
treward = 0
for i in range(1, L + 1):
    print("Level " + str(i))
    reward = 50 * i * i
    treward += reward
    print("Reward : " + str(reward) + " - Total rewards : " + str(treward))
