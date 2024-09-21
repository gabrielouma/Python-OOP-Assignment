# Create a Python class named Person.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# Implement a method called introduce that prints a message introducing the person with their name, age, and gender.

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Create an instance of the Person class and call the introduce method to display the person's information.

# Create an instance of the Person class
person1 = Person("Gabriel", 22, "Male")

# Call the introduce method
person1.introduce()