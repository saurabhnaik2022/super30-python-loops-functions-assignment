# Q18: Employee Salary Calculator - FUNCTION for the calculation, FOR loop for 5 employees
# Create a function that accepts employee name, basic salary, bonus percentage, and tax percentage. 
# Calculate gross salary, tax amount, and final salary. 
# Process at least five employees using a loop.

def calculate_salary(name, basic, bonus_pct, tax_pct):
    bonus = basic * bonus_pct / 100
    gross = basic + bonus
    tax = gross * tax_pct / 100
    final = gross - tax
    return {"name": name, "gross": gross, "tax": tax, "final": final}


employees = []
for i in range(1, 6):
    print(f"\nEmployee {i}")
    name = input("Name: ")
    basic = float(input("Basic salary: "))
    bonus_pct = float(input("Bonus %: "))
    tax_pct = float(input("Tax %: "))
    employees.append(calculate_salary(name, basic, bonus_pct, tax_pct))

print("\n--- Salary Report ---")
for e in employees:
    print(f"{e['name']}: Gross ₹{e['gross']:.2f} | Tax ₹{e['tax']:.2f} | Final ₹{e['final']:.2f}")
