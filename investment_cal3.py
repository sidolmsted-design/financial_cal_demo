#version 1

initial_investment = 1200
final_value = 10000

profit = final_value - initial_investment
return_pct = (profit - initial_investment) * 100

print("INVESTMENT CALCULATOR")
print(f"Initial Investment: ${initial_investment}")
print(f"Final Value: ${final_value}")
print(f"Profit: ${profit}")
print(f"Investment Return: {return_pct:.2f}%")


