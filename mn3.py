3.
import random   
num = random.randint(1, 10)
g = None   
while g != num:
    g = input("guess a number between 1 and 10: ")
    g = int(g)
    if g == num:
        print("congratulations! you won!")
        print(g)
        break
    else:
        print("nope, sorry. try again!")
print("Thank You :)")
