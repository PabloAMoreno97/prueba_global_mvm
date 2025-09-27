import os

from dotenv import load_dotenv

from create_employees_list import create_random_employee
from utils.database_utils import SessionLocal
from models.employee import Employee

load_dotenv()

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)


def add_employee(employee):
    try:
        session = SessionLocal()
        session.add(employee)
        session.commit()
    except Exception as e:
        print("Error while adding employee to the database:", e)

def list_employees():
    try:
        session = SessionLocal()
        employees = session.query(Employee).all()
        return employees
    except Exception as e:
        print("Error while listing employees from database:", e)


def get_employee_by_id(id):
    try:
        session = SessionLocal()
        employee = session.query(Employee).filter_by(id=id).first()
        print(employee)
    except Exception as e:
        print("Error while obtaining data for employee with ID {id}:", e)


if __name__ == "__main__":

    new_employee = create_random_employee()
    # add_employee(new_employee)
    employees_list = list_employees()
    employee = get_employee_by_id(13599)
