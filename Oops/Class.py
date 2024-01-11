class PersonalDetails:

    def __init__(self, name, age, height, weight, year = None):

        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def getName(self):

        return f"My name is {self.name}"
    
    def userName(self):

        return self.name + str(self.age)
    
    def setAge(self, new_age):

        self.age = new_age

        return self.age
    

    def Details(self):

        details = {
            "name": self.name
        }

        return details
    
        
person1 = PersonalDetails("Student1", 20, "170cm", 60.5)
print(person1.Details())
# person2 = PersonalDetails("Student2", 23, "188cm", 55.5)

# print(person1.getName())
# print(person1.age)
# print(person1.setAge(25))
# print(person1.age)
# print(person2.userName())









    

