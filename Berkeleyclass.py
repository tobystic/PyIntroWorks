from Berkeleyclassformat import Berkeleyclassformat


class Berkeleyclass:

    salutation = "Welcome to your new class: \n"
    print(salutation)

name = input('What is your Name? : ')
matricno = int(input('What is your matriculation no? : '))
hsstatus = bool(input('Have you completed high school- True or False? : '))
gender = input("Are you male or female? :")

newest1 = Berkeleyclassformat(name, matricno, hsstatus, gender)
print(newest1)
