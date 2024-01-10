# Program to calculate final cost with tax

# Get user input for the number of items and cost per item
num_items = int(input("Enter the number of items: "))
cost_of_item = float(input("Enter the cost of a single item: $"))

# Total cost without tax
cost_before_tax = num_items * cost_of_item

# Calculating tax
tax_rate = float(input("Enter the tax rate : "))
tax = cost_before_tax * tax_rate

# Total cost with tax
cost_after_tax = cost_before_tax + tax

# Display the results
print("\nResults:")
print("Cost before tax: ${:.2f}".format(cost_before_tax))
print("Tax : ${:.2f}".format(tax))
print("Cost after tax: ${:.2f}".format(cost_after_tax))
