4.
order = input("Enter your choice: ")
if order=="R"or"r":
    print("You have choose Reverse order.")
    s_p = int(input("Enter starting point: "))
    e_p = int(input("Enter ending point: "))
    print("r for Row order and c for Column order.")
    order2 = input("Enter your choice: ")
    if order2 == "r":
        print("You have choose Row order.")
        for x in range(s_p, e_p, -1):
            print(x, end = " ")
    elif order2 == "c":
        print("You have choose Column order.")
        for x in range(s_p, e_p, -1):
            print(x)
    else:
        print("You have choose Invalid choice.")
elif order == "F"or"f":
    print("You have choose Forward order.")
    s_p = int(input("Enter starting point: "))
    e_p = int(input("Enter ending point: "))
    print("r for Row order and c for Column order.")
    order2 = input("Enter your choice: ")
    if order2 == "r":
        print("You have choose Row order.")
        for x in range(s_p, e_p, 1):
            print(x, end = " ")
    elif order == "c":
        print("You have choose Column order.")
        for x in range(s_p, e_p, 1):
            print(x)
    else:
        print("You have choose Invalid choice.")
else:    
    print("You have choose Invalid choice.")
print("THANKYOU USER :)")

