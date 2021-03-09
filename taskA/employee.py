from person import Profile
import random


class Employee(Profile):
    def __init__(self, lastname, firstname, age):
        super().__init__(lastname, firstname, age)
        empid = self.generate_employee_id(firstname, lastname)
        self.__employee_id = empid

    def generate_employee_id(self, firstname, lastname):
        self.__employee_id = [firstname[0], lastname[0]]

        while len(self.__employee_id) < 8:
            number = random.randint(0, 9)
            self.__employee_id.append(str(number))
        return self.__employee_id

    def get_employee_profile(self):
        # tried to use super to call get profile
        return f"{super().getprofile()}  \nEmployee ID: {self.__employee_id}"


    def __str__(self):
        # tried to use super to call get profile
        return f"{super().getprofile()}  \nEmployee ID: {self.__employee_id}"
