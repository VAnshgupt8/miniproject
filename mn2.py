2.

inv={}
while True:
    print('''
          ADD==1
          REMOVE==2
          DISPLAY==3
          QUIT==4
          ''')
    action= int(input("enter your choice:-"))
    if action==1:
        item=input("enter item name:")
        quantity=int(input("enter your quantity:"))
        if item in inv:
            inv[item]+=quantity
        else:
            inv[item]=quantity
    elif action==2:
        item=input("enter the name of item you want to remove:")
        quantity=int(input("enter the quantity you want to remove:"))
        if item in inv and inv[item]>=quantity:
            inv[item]-=quantity
        elif item in inv and inv[item]<quantity:
            print(f"There are only {inv[item]} left in {item} left in inventory.")
        else:
            print("ther is no item left in inventory.")
    
    elif action==3:
        print("Inventory")
        for key,value in inv.items():
            print(f"{key}:{value}")
    
    elif action ==4:
        break
    else:
        print("invalid entry please try again")

