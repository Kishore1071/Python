class PersonalDetails:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def getName(self, year):

        return f"{self.name} and {year}"


person1 = PersonalDetails("Kishore", 25)

print(person1.getName(1998))



    

