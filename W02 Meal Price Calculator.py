# I added two more categories to the meals: drinks and desserts.

child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
drink_price = float(input("What is the price of a drink? "))
dessert_price = float(input("What is the price of a dessert? "))

num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))
num_drinks = int(input("How many drinks are there? "))
num_desserts = int(input("How many desserts are there? "))

tax_rate = float(input("What is the sales tax rate? "))


subtotal = (child_price * num_children) + (adult_price * num_adults) + (drink_price * num_drinks) + (dessert_price * num_desserts)

print()
# Subtotal
print ("Subtotal: $%.2f" % subtotal)

#Taxes
sales_tax = subtotal * (tax_rate / 100)
print ("Sales Tax: $%.2f" % sales_tax)

print()
# Total Price
total_price = subtotal + sales_tax
print ("Total Price: $%.2f" % total_price)

print()
# Payment
payment = float(input("What is the payment amount? "))
change = payment - total_price
print("Change: $%.2f" % change)

print()