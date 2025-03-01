player = input("whats ur name? ")
import random
score = 0
for i in range(3):
    print(f"round {i+1}")
    i += 1
    choice = input(" 1 = rock, 2 = paper or 3 = scissors? ")
    op = random.randint(1,3)
    print(f"{player} chose {choice} and the computer chose {op}")
    choice = int(choice)
    if choice > 3:
        print("OMG YOU USED GUN IT IS SUPER EFFECTIVE WOWZERS, sike you lose a point cheater")
        score -= 1
    elif choice == op:
        print("tie")
    elif choice > op:
        print("loss")
        score -= 1
    elif choice == 2 and op == 1:
        print("win")
        score += 1
    elif choice == 3 and op == 2:
        print("win")
        score += 1
    elif choice == 1 and op == 3:
        print("win")
        score += 1
    else:
        print("well that wasnt supposed to happen")
print(f"your final score was {score}")
if score > 0:
    print("you won")
else:
    print("you lost")
score = 0