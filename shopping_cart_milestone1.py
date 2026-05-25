# CSC500 Portfolio Milestone 1
# Digital Product Shopping Cart Initialization

# Gather product information from the user
product_name = input("Enter the product name: ")
product_price = float(input("Enter the product price: $"))
product_quantity = int(input("Enter the quantity: "))

# Perform calculations
subtotal = product_price * product_quantity
sales_tax = subtotal * 0.07
total_cost = subtotal + sales_tax

# Display shopping cart summary
print("\nShopping Cart Summary")
print("--------------------------")
print("Product:", product_name)
print("Price per Item: $", format(product_price, ".2f"))
print("Quantity:", product_quantity)
print("Subtotal: $", format(subtotal, ".2f"))
print("Sales Tax: $", format(sales_tax, ".2f"))
print("Total Cost: $", format(total_cost, ".2f"))