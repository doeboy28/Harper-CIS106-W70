ticker = input("Enter stock ticker symbol: ").upper()
shares = float(input("Enter number of shares: "))
cost_per_share = float(input("Enter cost per share: $"))
amount_invested = shares * cost_per_share
print(f"Stock: {ticker}")
print(f"Amount invested: ${amount_invested:.2f}")
