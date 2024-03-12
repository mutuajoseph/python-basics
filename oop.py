# CLASS - Its a blueprint of an object(An instance of a class)

# HOW TO CREATE A CLASS

class Person:

    # person attribute 
    name = ""
    age = 0 
    color = ""
    body_mass = 0 

    # walk, eat, run, shout, cry 
    @classmethod
    def walk(cls, person_instance):
        print(f" {person_instance.name} who is a person has started walking")

    @staticmethod
    def eat(person_instance):
        print(f" {person_instance.name} who is a person is about to eat")


# How to create an object 
person_one = Person()
person_one.name = "Clare Oparo"
person_one.age = 50
person_one.color = "chocolate"
person_one.body_mass = 60

person_two = Person()
person_two.name = "Mariam Senzia"
person_two.age = 26
person_two.color = "lightskin"
person_two.body_mass = 60

print(f"{person_one.name} is {person_one.age} years of age")
print(f"{person_two.name} is {person_two.age} years of age")

person_one.walk(person_one)
person_two.walk(person_two)

person_one.eat(person_one)