class Profile:
    def __init__(self, name, age):
        self._fullname = name
        self._age = age

    def inputfirstname(self, firstname):
        self._fullname += firstname

    def inputlastname(self, lastname):
        self._fullname += " "
        self._fullname += lastname

    def inputage(self, age):
        self._age = int(age)

    def getprofile(self):
        return f"Name: {self._fullname} \nAge: {str(self._age)}"
