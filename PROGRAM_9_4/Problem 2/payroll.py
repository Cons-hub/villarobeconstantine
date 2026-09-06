def calculate_tax(gross_pay):
    return gross_pay * 0.10


def calculate_net_pay(gross_pay, tax):
    return gross_pay - tax


def display_payroll(employee, gross_pay, tax, net_pay):
    print("\n===== EMPLOYEE PAYROLL =====")
    print("Employee ID:", employee.employee_id)
    print("Employee Name:", employee.name)
    print(f"Hourly Rate: ₱{employee.hourly_rate:.2f}")
    print(f"Hours Worked: {employee.hours_worked:.2f}")
    print(f"Gross Pay: ₱{gross_pay:.2f}")
    print(f"Tax Deduction (10%): ₱{tax:.2f}")
    print(f"Net Pay: ₱{net_pay:.2f}")