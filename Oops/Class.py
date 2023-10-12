class PersonalDetails:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def getName(self):

        return self.name
    
    def setAge(self, new_age):

        self.age = new_age

        return self.age


person1 = PersonalDetails("Kishore", 25)

print(person1.getName())
print(person1.setAge(26))





    

