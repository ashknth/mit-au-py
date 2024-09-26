# -*- coding: utf-8 -*-
"""HumanResource

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fd94husNqxYct_rdavb-5e3af7tZzqGg
"""

class Employee:
    def __init__(self, emp_id, name, role):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.hours_worked = 0
        self.overtime_hours = 0
        self.unavailable_hours = 0
        self.training_hours = 0
        self.promoted = False
        self.on_vacation = False

    def work(self, hours):
        self.hours_worked += hours

    def log_overtime(self, hours):
        self.overtime_hours += hours

    def mark_unavailable(self, hours):
        self.unavailable_hours += hours

    def log_training(self, hours):
        self.training_hours += hours

    def promote(self):
        self.promoted = True

    def start_vacation(self):
        self.on_vacation = True

    def end_vacation(self):
        self.on_vacation = False

class HRManager:
    def __init__(self):
        self.employees = {}
        self.to_be_hired = []

    def add_employee(self, emp_id, name, role):
        self.employees[emp_id] = Employee(emp_id, name, role)

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]

    def hire_employee(self, name, role):
        self.to_be_hired.append((name, role))

    def start_vacation(self, emp_id):
        if emp_id in self.employees:
            self.employees[emp_id].start_vacation()

    def end_vacation(self, emp_id):
        if emp_id in self.employees:
            self.employees[emp_id].end_vacation()

    def log_hours(self, emp_id, hours):
        if emp_id in self.employees:
            self.employees[emp_id].work(hours)

    def log_overtime(self, emp_id, hours):
        if emp_id in self.employees:
            self.employees[emp_id].log_overtime(hours)

    def log_unavailable_hours(self, emp_id, hours):
        if emp_id in self.employees:
            self.employees[emp_id].mark_unavailable(hours)

    def log_training_hours(self, emp_id, hours):
        if emp_id in self.employees:
            self.employees[emp_id].log_training(hours)

    def promote_employee(self, emp_id):
        if emp_id in self.employees:
            self.employees[emp_id].promote()

    def display_employee_info(self, emp_id):
        if emp_id in self.employees:
            emp = self.employees[emp_id]
            print(f"Employee ID: {emp.emp_id}")
            print(f"Name: {emp.name}")
            print(f"Role: {emp.role}")
            print(f"Hours Worked: {emp.hours_worked}")
            print(f"Overtime Hours: {emp.overtime_hours}")
            print(f"Unavailable Hours: {emp.unavailable_hours}")
            print(f"Training Hours: {emp.training_hours}")
            print(f"On Vacation: {'Yes' if emp.on_vacation else 'No'}")
            print(f"Promoted: {'Yes' if emp.promoted else 'No'}")
            print("\n")

    def display_to_be_hired(self):
        print("Employees to be Hired:")
        for name, role in self.to_be_hired:
            print(f"Name: {name}, Role: {role}")

# Example usage
if __name__ == "__main__":
    hr_manager = HRManager()

    # Add some employees
    hr_manager.add_employee(1, "John Doe", "Developer")
    hr_manager.add_employee(2, "Jane Smith", "Designer")

    # Log hours worked
    hr_manager.log_hours(1, 40)
    hr_manager.log_overtime(1, 5)
    hr_manager.log_training_hours(2, 8)

    # Start and end vacation
    hr_manager.start_vacation(2)
    hr_manager.end_vacation(2)

    # Promote an employee
    hr_manager.promote_employee(1)

    # Display employee info
    hr_manager.display_employee_info(1)
    hr_manager.display_employee_info(2)

    # Hire new employees
    hr_manager.hire_employee("Alice Johnson", "Product Manager")
    hr_manager.hire_employee("Bob Lee", "QA Engineer")
    hr_manager.display_to_be_hired()