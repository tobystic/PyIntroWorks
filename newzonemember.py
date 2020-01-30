class newzonemember:

    def __init__(self, name, gender, age, zipnumber):

        self._name = name
        self._gender = gender
        self._age = age
        self._zipnumber = zipnumber

    """define set and get attribute"""

    def get_name(self):
        return self._name

    def get_gender(self):
        return self._gender

    def get_age(self):
        return age

    def get_zipnumber(self):
        return zipnumber

    def set_name(self, name):
        self._name = name

    def set_gender(self, gender):
        self._gender = gender

    def set_age(self, age):
        self._age = age

    def set_zipnumber(self,zipnumber):
        self._zipnumber = zipnumber

    def __str__(self):
        return "Welcome to 13th Ave W, OceanView apartments" "\nName: " + self._name + "\nGender: " + self._gender + "\nage: " + str(self._age) + "\nZipcodeno: " + str(self._zipnumber)

newoccupant = newzonemember("Arthur", "Male", "32", "98119")
print(newoccupant)

