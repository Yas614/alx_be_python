income = float(input("Enter your monthlu income: "))
expenses = float(input("Enter your total monthly expenses: "))

monthly_saving = income-expenses
annual_saving = monthly_saving*12
interest = annual_saving*0.05
projected_annual_savings = annual_savings + interest

print(f"\nYour monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings with 5% interest is: ${projected_annual_savings:.2f}")

