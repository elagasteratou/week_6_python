from customer import Profile

class Employee(Profile):
    def __init__(self, name, age, employee_id):
        self._employee_id = employee_id
        super().__init__(name, age)

    def inputemployee_id(self, employee_id):
        self._employee_id = employee_id

    def getprofile(self):
        return f"Name: {self._fullname} \nAge: {str(self._age)} \nEmployee ID: {self._employee_id}"

