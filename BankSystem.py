class Employee:
    def __init__(self, id, name, lastname, position, area, gross_salary):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.position = position
        self.area = area
        self.gross_salary = gross_salary

    def calculate_net_salary(self):
        net_salary = self.gross_salary - (self.gross_salary * 0.2)
        return net_salary

    def generate_pay_stub(self):
        net_salary = self.calculate_net_salary()
        pay_stub = f"Pay Stub\n" \
                   f"ID: {self.id}\n" \
                   f"Name: {self.name} {self.lastname}\n" \
                   f"Position: {self.position}\n" \
                   f"Area: {self.area}\n" \
                   f"Gross Salary: ${self.gross_salary}\n" \
                   f"Net Salary: ${net_salary}"
        return pay_stub

employees = []

def register_employee():
    id = int(input("Employee ID: "))
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    position = input("Position: ")
    area = input("Area: ")
    gross_salary = float(input("Gross Salary: "))

    employee = Employee(id, first_name, last_name, position, area, gross_salary)
    employees.append(employee)
    print("Employee registered successfully!")

def list_employees():
    print("\nList of Employees:")
    for employee in employees:
        print(f"ID: {employee.id}, Name: {employee.name} {employee.lastname}")

def view_pay_stub():
    id = int(input("Enter the Employee ID: "))
    for employee in employees:
        if employee.id == id:
            pay_stub = employee.generate_pay_stub()
            print(pay_stub)
            break
    else:
        print("Employee not found.")

while True:
    print("\nOptions:")
    print("1. Register Employee")
    print("2. List Employees")
    print("3. View Pay Stub")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        register_employee()
    elif option == "2":
        list_employees()
    elif option == "3":
        view_pay_stub()
    elif option == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
