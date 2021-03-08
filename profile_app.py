from person import Profile
from employee import Employee


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


def get_customer_details():
    firstname = input("Please input your first name:")
    lastname = input("Please input your last name:")
    age = input("Please input your age:")

    customer_profile = Profile(firstname="", lastname="", age=0)

    customer_profile.inputfirstname(firstname)
    customer_profile.inputlastname(lastname)
    customer_profile.inputage(age)

    customer_profile_details = customer_profile.getprofile()

    print(f"\n{customer_profile_details}")


print("\nEmployee profiles\n")
get_employee_details()

print("\nCustomer profiles\n")
# get_customer_details()

# print("\nPerson profiles\n")
