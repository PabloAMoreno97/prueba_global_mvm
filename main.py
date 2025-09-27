import random as rd
import pandas as pd

from constants import Department, Position, column_names_for_csv
from employee import Employee


def create_random_employee() -> Employee:
    try:
        print("Creating random employee")

        department = Department(rd.randint(0, len(Department)-1))
        position = Position(rd.randint(0, len(Position)-1))
        name = f"Empleado {rd.randint(0, 10**5)}"
        employee = Employee(department, position, name)

        print("Created employee:", employee)
        return employee

    except Exception as e:
        print("Error while creating a random employee:", e)


def create_employees_list(list_size: int) -> pd.DataFrame:
    try:
        if list_size > 0:
            employees_list = [create_random_employee().to_tuple() for _ in range(list_size)]
            return pd.DataFrame(employees_list, columns=column_names_for_csv)
        else:
            raise Exception("List size must be greater than zero")
    except Exception as e: 
        print("Error while creating employees list:", e)


if __name__ == "__main__":
    print(create_employees_list(25))
