class Eiecovenant:

    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_gender(self):
        return self._gender

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_gender(self, gender):
        self._gender = gender

    def __str__(self):
        return "EIE Covenant \nName :" + self._name + "\nAge :" + str(self._age) + "\nGender :" + self._gender


student1 = Eiecovenant("Chinedu", 29, "Male")
print(student1)

if student1.get_age() > 30:
    print(student1.get_name() + " is too young for this class")
else:
    print("Welcome to EIE 2008 Class " + student1.get_name() + " !!!")


