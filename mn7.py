import random as r
rep = True
while rep:
    print("You rolled",r.randint(1,6))
    print("Do you want to roll again? Y/N")
    rep = "Y"in input()
