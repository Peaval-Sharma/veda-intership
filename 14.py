# Shopping Bill Generator

products = []

n = int(input("Enter number of products: "))

for i in range(n):
    name = input(f"\nEnter product {i + 1} name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    total = quantity * price

    product = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "total": total
    }

    products.append(product)


# Calculate subtotal
subtotal = 0

for product in products:
    subtotal += product["total"]


# Discount
discount = subtotal * 0.10

# Amount after discount
amount_after_discount = subtotal - discount

# Tax (5%)
tax = amount_after_discount * 0.05

# Final amount
final_amount = amount_after_discount + tax


# Print Bill
print("\n" + "=" * 45)
print("              SHOPPING BILL")
print("=" * 45)

print(f"{'Product':<15}{'Qty':<8}{'Price':<10}{'Total':<10}")
print("-" * 45)

for product in products:
    print(f"{product['name']:<15}"
          f"{product['quantity']:<8}"
          f"{product['price']:<10.2f}"
          f"{product['total']:<10.2f}")

print("-" * 45)

print(f"Subtotal          : ₹{subtotal:.2f}")
print(f"Discount (10%)    : ₹{discount:.2f}")
print(f"Tax (5%)          : ₹{tax:.2f}")
print(f"Final Amount      : ₹{final_amount:.2f}")

print("=" * 45)
print("       Thank You for Shopping!")
print("=" * 45)