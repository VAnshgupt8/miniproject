import random as r
def check(c, us):
    if c == us:
        return 0
    if(c== 0 and us == 1):
        return -1
    if (c == 1 and us == 2):
        return -1
    if (c== 2 and us == 0):
        return -1
    return 1
c = r.randint(0, 2)
us = int(input("0 for rock, 1 for paper and 2 for scissor:"))
s = check(c, us)
print("You: ", us)
print("Computer: ", c)
if s == 0:
    print("It's Draw.")
elif s == -1:
    print("You Loose.")
elif s==1:
    print("You Won.")


