menu = {"pizza": 100,
        "burger": 50, 
        "pasta": 80, 
        "salad": 30, 
        "coffee": 60
        }
print ("Welcome to the Hotel Menu!" )
print("pizza: 100\nburger: 50\npasta: 80\nsalad: 30\ncoffee: 60")
order_total = 0
#80 + 70 = 150
item_1 = input("Enter the first item you want to order = ")
if item_1 in menu :
    order_total += menu[item_1] #0 + 50
    print(f"your item {item_1} has been added to you order ")
else:
    print(f"Ordered item {item_1} is not available yet !")

another_order = input("Do you want another item ? (yes/no):")
if another_order.lower() == "yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available!")
print(f"The total amount of items to pay is {order_total}")