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

# Version 1 & 2: Basic Investment Calculator
initial_investment = 10000
final_value = 1200
profit = final_value - initial_investment
return_pct = (profit / initial_investment) * 100

# Version 2 additions:
years = 5
annualized_return = ((final_value/initial_investment)**(1/years)-1) * 100

print("INVESTMENT CALCULATOR")
print(f"Initial Investment: ${initial_investment}")
print(f"Final Value: ${final_value}")
print(f"Profit: ${profit}")
print(f"Investment Return: {return_pct:.2f}%")
print(f"Annualized Return: {annualized_return:.2f}%")
