class PersonalDetails:

    def __init__(self, name, age, year):

        self.name = name
        self.age = age
        self.year = year

    def getUserName(self):

        return self.name + str(self.age) + str(self.year)

class ProfessionalDetails(PersonalDetails):

    def __init__(self, name, age, number, designation):
        super().__init__(name, age, number)

        self.designation = designation

    def getDesignation(self):

        return self.designation

professional = ProfessionalDetails("Kishore", 25, 1998, "Software Developer")

print(professional.getUserName())
print(professional.getDesignation())