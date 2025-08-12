# Set up the lists and dictionaries.
menu = ["Burger","Pizza","Hotdog","Sub"]
stock = {"Burger":8,
         "Pizza":4,
         "Hotdog":5,
         "Sub":11}
price = {"Burger":85.99,
         "Pizza":99.99,
         "Hotdog":65.99,
         "Sub":79.99}

# Declare the total_stock variable.
total_stock = 0.00
print("Stock Taking")
# Iterate through the dictionaries, adding the sum total of each item to the total_stock variable.
for item in menu:
    total_stock += int(stock[item]) * float(price[item])
    print(f"{item}:\tR {price[item]}\tx\t{stock[item]}\t=\tR {price[item]*stock[item]}")
print(f"Total:\t\t\t\t\tR {total_stock}")