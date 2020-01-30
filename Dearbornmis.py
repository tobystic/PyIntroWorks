class Dearbornmis:


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
        return "U of M Dearborn 2016\n" "Student Name: " + self._name + "\nAge: " + str(self._age) +"\nGender: " + self._gender


#newstudent = Dearbornmis("Tobi", "male", "35")
#print(newstudent)
#print("")
#print(newstudent.get_age())
#print(f"the value of 10/7 is : {10/7}")


