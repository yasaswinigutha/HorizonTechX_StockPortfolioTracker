Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

portfolio = {}
total_value = 0

print("=== Stock Portfolio Tracker ===")

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock_name = input("\nEnter stock name (AAPL/TSLA/GOOGL/MSFT/AMZN): ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        portfolio[stock_name] = quantity
        investment = stock_prices[stock_name] * quantity
        total_value += investment

        print(f"Investment in {stock_name}: ${investment}")

    else:
        print("Stock not found in price list!")

print("\n----- Portfolio Summary -----")

for stock, qty in portfolio.items():
    print(f"{stock} : {qty} shares @ ${stock_prices[stock]}")

print(f"\nTotal Investment Value = ${total_value}")

# Save results to a text file
with open("portfolio.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("-----------------\n")

    for stock, qty in portfolio.items():
        file.write(f"{stock} : {qty} shares @ ${stock_prices[stock]}\n")

    file.write(f"\nTotal Investment Value = ${total_value}")

print("\nPortfolio saved successfully in 'portfolio.txt'")
