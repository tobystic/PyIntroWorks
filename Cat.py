class Cat:

    def __init__(self, name, breed, age):
        self._name = name
        self._breed = breed
        self._age = age

    def get_name(self):
        return self._name

    def get_breed(self):
        return self._breed

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def set_breed(self, breed):
        self._breed = breed

    def set_age(self, age):
        self._age = age
    #tostring to class cat when called
    def __str__(self):
        return "Cat Bio \n======= \nName : " + self._name + "\nBreed : " + self._breed + "\nAge : " + str(self._age)


cat1 = Cat("Schrodinger", "Chesire", 31)
print(cat1)

print("Breedingmay be suspended due to the CoronaVirus")
