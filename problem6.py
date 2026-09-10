purchase_price = float(input("Enter purchase price per share: $"))
current_price = float(input("Enter current stock price: $"))
quantity = float(input("Enter quantity of stock: "))

value_change = (current_price - purchase_price) * quantity

print(f"Increase/decrease in stock value: ${value_change:.2f}")

if value_change < 0:
    print("You are losing money.")
elif value_change > 0:
    print("You are making money.")
else:
    print("There is no change in value.")
