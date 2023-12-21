import random

num_options = [1,2,3,4,5,6]
toss_options = ['ODD', 'EVEN']
player_role = ['BAT', 'BALL']

def choice():
    while True:
        user_choice = int(input("Enter a number between 1-6 : "))
        if user_choice not in num_options:
            print("Invalid Input!\nRenter")
            print("-----------------------------------------------")
        else:
            break
    return user_choice

def toss():
    while True:
        user_toss=input("Choose \'ODD\' or \'EVEN\' : ").upper()
        if user_toss not in toss_options:
            print("Invalid Input!\nRenter")
            print("-----------------------------------------------")
        else:
            break
    return user_toss

def role_selection(role):
    if role == 'BAT':
        return 'BALL'
    else:
        return 'BAT'

def compare_choice(val, user_toss):
    if val == user_toss:
        print("\nUser won the toss\n")
        user_role = input("Choose BAT or BALL : ").upper()
        comp_role = role_selection(user_role)
        print("User chose to :", user_role, "& Computer will :", comp_role, '\n')
    else:
        print("Computer won the toss")
        comp_role = random.choice(player_role)
        user_role = role_selection(comp_role)
        print("Computer chose to :", comp_role, "& User will :", user_role, '\n')

    return [user_role, comp_role]

def first_batting(player):
    runs = 0
    while True:
        comp_choice = random.choice(num_options)
        user_choice = choice()
        print("computer chose :", comp_choice)
        if comp_choice != user_choice and player == 'user':
            runs += user_choice
        elif comp_choice != user_choice and player == 'computer':
            runs += comp_choice
        else:
            print('\n', player, "is out. Innings over!!!\n")
            break
        print("Score =", runs)
    return runs

def second_batting(player, prev_score):
    runs = 0
    p2_status = True
    while runs <= prev_score:
        comp_choice = random.choice(num_options)
        user_choice = choice()
        print("computer chose :", comp_choice)
        if comp_choice != user_choice and player == 'user':
            runs += user_choice
        elif comp_choice != user_choice and player == 'computer':
            runs += comp_choice
        else:
            p2_status = False
            if runs == prev_score:
                print("Match draw...")
            else:
                if player == 'user':
                    print("\ncomputer won the game")
                else:
                    print("\nuser won the game")
                break
        print("Score =", runs)

    if p2_status == True:
        print('\n', player, "won the game")
    
def play(user):
    # Player 1 batting
    if user == 'BAT':
        user_score = first_batting('user')
        print("user score :", user_score)
        print("Computer needs", user_score+1, "runs to win\n")
        user = 'BALL'
    else:
        comp_score = first_batting('computer')
        print("computer score :", comp_score)
        print("User needs", comp_score+1, "runs to win\n")
        user = 'BAT'

    # Player 2 batting
    if user == 'BAT':
        second_batting('user', comp_score)
    else:
        second_batting('computer', user_score)


print("Let the toss begin\n")
user_toss = toss()
user_choice = choice()
comp_choice = random.choice(num_options)
print("Computer chose :", comp_choice)
toss_value = user_choice + comp_choice

if toss_value % 2 == 0:
    roles = compare_choice('EVEN', user_toss)
else:
    roles = compare_choice('ODD', user_toss)

user = roles[0]
comp = roles[1]

play(user)