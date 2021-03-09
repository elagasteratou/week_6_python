from person import Profile
from employee import Employee
from customer import Customer


# employee profiles


def get_employee_details():
    firstname = input("Please input your first name:")
    lastname = input("Please input your last name:")

    age = input("Please input your age:")
    # add function to validate age and ensure they are numbers

    employee_profile = Employee("", "", "", "")

    employee_profile.generate_employee_id(firstname, lastname)
    employee_profile.inputfirstname(firstname)
    employee_profile.inputlastname(lastname)
    employee_profile.inputage(age)

    employee_profile_details = employee_profile.get_employee_profile()

    print(employee_profile_details)


def get_person_details():
    firstname = input("Please input your first name:")
    lastname = input("Please input your last name:")
    age = input("Please input your age:")

    person_profile = Profile(firstname="", lastname="", age=0)

    person_profile.inputfirstname(firstname)
    person_profile.inputlastname(lastname)
    person_profile.inputage(age)

    person_profile_details = person_profile.getprofile()

    print(f"\n{person_profile_details}")


def get_customer_details():
    firstname = input("Please input your first name:")
    lastname = input("Please input your last name:")
    age = input("Please input your age:")

    customer_profile = Customer(firstname="", lastname="", age=0, customer_id = [])

    customer_profile.inputfirstname(firstname)
    customer_profile.inputlastname(lastname)
    customer_profile.inputage(age)
    customer_profile.generate_customer_id(firstname, lastname)

    customer_profile_details = customer_profile.get_customer_profile()

    print(customer_profile_details)


print("\nEmployee profiles\n")
# get_employee_details()

print("\nPerson profile\n")
# get_person_details()
print("\nCustomer profiles\n")

get_customer_details()




