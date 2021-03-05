from customer import Profile
from employee import Employee

lisa_profile = Profile(name = "", age = 0)

lisa_profile.inputfirstname("Lisa")
lisa_profile.inputlastname("Simpson")
lisa_profile.inputage("10")

# employee profiles
mg_profile = Employee(name = "", age = 0, employee_id = "")
mg_profile.inputfirstname("Michaela")
mg_profile.inputlastname("Gasteratou")
mg_profile.inputage("26")
mg_profile.inputemployee_id("MG112ID56")
print(mg_profile.getprofile())
