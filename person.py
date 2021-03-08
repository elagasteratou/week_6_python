class Profile:
    def __init__(self, firstname, lastname, age):
        self._firstname = firstname
        self._lastname = lastname
        self._age = age

    def inputfirstname(self, firstname):
        self._firstname += firstname

    def inputlastname(self, lastname):
        self._lastname += lastname

    def inputage(self, age):
        self._age = int(age)

    def getprofile(self):
        return f"Name: {self._firstname} {self._lastname} \nAge: {str(self._age)}"
