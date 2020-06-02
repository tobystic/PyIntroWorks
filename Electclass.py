class Electclass:


    def __init__(self,name, gender, age):
        self._name = name
        self._gender = gender
        self._age = age

    def get_name(self):
        return self._name

    def get_gender(self):
        return self._gender

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def set_gender(self, gender):
        self._gender = gender

    def set_age(self, age):
        self._age = age

    def __str__(self):
        return "E/E Class 2008 \n----------------\nName :" + self._name + "\nGender :" + self._gender + "\nAge :" + str(self._age)

    #print("Hello")

    #name1 = input("what is your name :")
    #gender1 = input("what is your gender? m or f:")
    #age1 = int(input("How old do you turn on your next birthday?")

fresher1 = Electclass("wunmi","m","33")
print(fresher1)
