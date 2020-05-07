from Dearbornmis import Dearbornmis


class Misclass:

    salut = """
        #######################################################################################################################
        #######################################################################################################################
        ####                                                                                                               ####
        ####                               WELCOME TO THE UNIVERSITY OF MICHIGAN, DEARBORN                                 ####
        ####                                                                                                               ####
        #######################################################################################################################
        #######################################################################################################################
            """

    print(salut)
name = input('What is your Name? : ')
age = int(input('How old are you going to be for your next birthday? : '))
gender = input('Are you male or female? : ')

newstudent = Dearbornmis(name, age, gender)
print("\n")
print("----------------------------------------------------------------------------------------------------")
print(newstudent)
print("\n")
if newstudent.get_age() < 30:
    print("You are unable to enrol for this class due to incomplete pre-requisite")
else:
    print("Welcome to Fall semester")

