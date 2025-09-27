from enum import Enum


class Department(Enum):
    TI = 0
    FINANCE = 1
    MARKETING = 2
    HUMAN_RESOURCES = 3
    PRODUCTION = 4
    SALES = 5
    LOGISTICS = 6


class Role(Enum):
    DEVELOPER = 0
    DIRECTOR = 1
    MANAGER = 2
    ACCOUNTANT = 3
    ENGINEER = 4
    HUMAN_TALENT = 5
    ANALYST = 6


column_names_for_csv = ["id", "role", "department"]

s3_bucket = "prueba-global-mvm"
s3_data_folder = "data"
file_name = "employees.parquet"
