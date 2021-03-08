from person import Profile


class Employee(Profile):
    def __init__(self, lastname, firstname, age, employee_id):
        self.__employee_id = employee_id
        super().__init__(lastname, firstname, age)

    def inputemployee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_employee_profile(self):
        # tried to use super to call get profile
        return f"{super().getprofile()}  \nEmployee ID: {self.__employee_id}"
