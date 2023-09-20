purchases = int(input("Number of purchases: "))
tax_percent = float(input("Sales tax: "))
tax = tax_percent / 100  

customers = []
items = []

for i in range(purchases):
    name = input("Enter name of customer: ")
    item = float(input("Cost: "))
    customers.append(name)
    items.append(item)

def add_tax(list_items, tax):
    taxed_items = []
    for item in list_items:
        taxed_items.append(item * (1 + tax))
    return taxed_items

taxed_prices = add_tax(items, tax)

total_purchases = {}

for i in range(purchases):
    if customers[i] not in total_purchases:
        total_purchases[customers[i]] = 0
    total_purchases[customers[i]] += taxed_prices[i]

print(total_purchases)
