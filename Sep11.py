# boolean
hot = False
summer = True

# challenge 2

appetizer = float(input("Cost of appetizer(no dollar sign): "))
entree = float(input("Cost of entree(no dollar sign): "))
dessert = float(input("Cost of dessert(no dollar sign): "))

subtotal = float(appetizer + entree + dessert)
tax = float(subtotal * .0825)
tip = float(subtotal * .18)
grand_total = float(subtotal + tax + tip)

print("Subtotal: " + str(subtotal))
print("Tax: " + str(tax))
print("Tip: " + str(tip))
print("Grand Total: " + str(grand_total))