class PersonalDetails:

    def __init__(self, name, age, height, weight):

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


person1 = PersonalDetails(age = 25, name="Kishore", height=None, weight=34)
person2 = PersonalDetails("Srikanth", 25, None, 43)
person3 = PersonalDetails("Sathish", 25, None, 23)
person4 = PersonalDetails("Vittchu", 25, None, 55)
# print(person2.name, ",name from class")
# print(person2.height, ",height from class")
print(person2.getName())
print(person2.userName())
print(person2.setAge(22))
print(person2.userName())


def GetName(person_name):

    return f"My name is {person_name}"


person1 = {
    "name": "Kishore",
    "age": 25,
    "height": 170,
    "weight": 50
}
person2 = {
    "name": "Srikanth",
    "age": None,
    "height": 170,
    "weight": 50
}   
person3 = {
    "name": "Kishore",
    "age": 25,
    "height": 170,
    "weight": 50
}
person4 = {
    "name": "Srikanth",
    "age": 22,
    "height": 170,
    "weight": 50
}

# print(person1['name'], ",name manul")
# print(person1['height'], ",height manul")
print(GetName(person1["name"]))
print(GetName("Blue"))





    

