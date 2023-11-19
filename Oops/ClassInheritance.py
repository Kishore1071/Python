class PersonalDetails:

    def __init__(self, name, age, year):

        self.name = name
        self.age = age
        self.year = year

    def getUserName(self):

        return self.name + str(self.age) + str(self.year)

class ProfessionalDetails(PersonalDetails, ):

    def __init__(self,name, age, year, designation):
        super().__init__(name, age, year)

        self.designation = designation

    def getDesignation(self):

        return f"{self.name} is working as a {self.designation}"

professional = ProfessionalDetails("Kishore", 25, 1998, "Software Developer")

print(professional.designation)

print(professional.getUserName())
print(professional.getDesignation())

person2 = ProfessionalDetails("person_data", 23, 56423, "Job")

print(person2.getUserName)