import random as rd
import pandas as pd

from utils.constants import (Department, Role, column_names_for_csv, s3_data_folder, 
                       s3_bucket, file_name)
from models.employee import Employee


def create_random_employee() -> Employee:
    try:
        print("Creating random employee")

        id = rd.randint(0, 10**5)
        role = Role(rd.randint(0, len(Role)-1))
        department = Department(rd.randint(0, len(Department)-1))
        employee = Employee(id, role, department)

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


def save_employees_list_on_s3(employees_df: pd.DataFrame):
    try:
        s3_path = f"s3://{s3_bucket}/{s3_data_folder}/{file_name}"
        employees_df.to_parquet(s3_path, engine="pyarrow", index=False)
        print("Archivo guardado en S3:", s3_path)
    except Exception as e:
        print(f"Error while saving {file_name} on S3:", e)


if __name__ == "__main__":
    employees_df = create_employees_list(25)
    save_employees_list_on_s3(employees_df)
