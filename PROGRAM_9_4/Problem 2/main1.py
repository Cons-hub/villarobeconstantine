from employee import Employee
from payroll import calculate_tax, calculate_net_pay, display_payroll


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Value cannot be negative.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("===== EMPLOYEE PAYROLL CALCULATOR =====")

    name = input("Enter employee name: ").strip()
    employee_id = input("Enter employee ID: ").strip()

    hourly_rate = get_positive_number("Enter hourly rate: ₱")
    hours_worked = get_positive_number("Enter hours worked: ")

    employee = Employee(
        name,
        employee_id,
        hourly_rate,
        hours_worked
    )

    gross_pay = employee.calculate_gross_pay()
    tax = calculate_tax(gross_pay)
    net_pay = calculate_net_pay(gross_pay, tax)

    display_payroll(
        employee,
        gross_pay,
        tax,
        net_pay
    )


if __name__ == "__main__":
    main()