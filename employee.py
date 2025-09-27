from constants import Department, Position

class Employee():

    def __init__(self, department: Department, position: Position, name: str):
        self.__department = department
        self.__position = position
        self.__name = name

    def __repr__(self):
        return f"{self.__name} - {self.__position} - {self.__department}"


    def to_tuple(self):
        return (self.__name, self.__position.name, self.__department.name)
