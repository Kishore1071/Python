class PersonalDetails:

    def __init__(self, name, age, number):

        self.name = name
        self.age = age
        self.number = number

    def getUserName(self):

        return self.name + str(self.age) + str(self.number)

class ProfessionalDetails(PersonalDetails):

    def __init__(self, name, age, number, designation):
        super().__init__(name, age, number)

        self.designation = designation

    def getDesignation(self):

        return self.designation + " " + self.name

professional = ProfessionalDetails("Kishore", 25, 1998, "Software Developer")

print(professional.getUserName())
print(professional.getDesignation())