from enum import Enum


class Department(Enum):
    TI = 0
    FINANCE = 1
    MARKETING = 2
    HUMAN_RESOURCES = 3
    PRODUCTION = 4
    SALES = 5
    LOGISTICS = 6


class Position(Enum):
    DEVELOPER = 0
    DIRECTOR = 1
    MANAGER = 2
    ACCOUNTANT = 3
    ENGINEER = 4
    HUMAN_TALENT = 5
    ANALYST = 6


column_names_for_csv = ["Name", "Position", "Deparment"]
