file = open('sales.csv', 'r')
sales = file.read().split('\n')
customers = {}
for line in sales:
    customer, product, count = line.split()
    customers.setdefault(customer, {})[product] = int(count)
for customer in sorted(customers):
    products = sorted(customers[customer])
    print('Customer:', customer)
    print('Products:', products)
    print()