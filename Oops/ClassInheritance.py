class PersonalDetails:

    def __init__(self, name, age, year):

        self.name = name
        self.age = age
        self.year = year

    def getUserName(self):

        return self.name + str(self.age) + str(self.year)
    
class Family:

    pass

class ProfessionalDetails(PersonalDetails, Family):

    def __init__(self, name, age, year, designation):
        super().__init__(name, age, year)
     
        self.designation = designation

    def getDesignation(self):

        return f"{self.name} is working as a {self.designation}"
    
person1 = ProfessionalDetails("Student1", 25, 1998, "Student")

print(person1.designation)
print(person1.name)
print(person1.getUserName())
print(person1.getDesignation())

