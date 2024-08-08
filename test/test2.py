print("################Menu################")
print("##### 1. Coffee   2. Coco   3. Tea #####")
print("####################################")
selectMenu = int(input('CHOOSE MENU : [1-3] : '))

if selectMenu == 1:
    menu = 'Coffee'
    cost = 51
elif selectMenu == 2:
    menu = 'Coco'
    cost = 42
elif selectMenu == 3:
    menu = 'Tea'
    cost = 27
else:
    print("Invalid selection. Please try again.")

print(f"Selected: {menu}")
print(f"Cost: {cost}")

total_inserted = 0
while total_inserted < cost:
    try:
        coin = int(input("Please insert coin : [1, 2, 5, 10] "))
        if coin in [1, 2, 5, 10]:
            total_inserted += coin
            remaining = cost - total_inserted
            if remaining > 0:
                print(f"Please insert: {remaining}")
            else:
                change = abs(remaining)
                if change > 0:
                    print(f"Returning change: {change}")
        else:
            print("Invalid coin value.")
    except ValueError:
        print("Please insert a valid coin.")


print(f"Enjoy your {menu}!")
print("################ END ################")

