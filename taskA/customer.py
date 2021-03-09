from person import Profile
from employee import Employee
import random

class Customer(Profile):
    def __init__(self, lastname, firstname, age, customer_id):
        self.__customer_id = customer_id
        super().__init__(lastname, firstname, age)

    def generate_customer_id(self, firstname, lastname):
        # return super().generate_employee_id(firstname, lastname)
        self.__customer_id = [firstname[0], lastname[0]]

        while len(self.__customer_id) < 8:
            number = random.randint(0, 9)
            self.__customer_id.append(str(number))
        return self.__customer_id

    def get_customer_profile(self):
        return f"{super().getprofile()}\nCustomer ID: {self.__customer_id}"
