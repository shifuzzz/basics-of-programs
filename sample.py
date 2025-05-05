class Dog:
    # This is the class constructor
    def __init__(self, breed, age, color):
        self.breed = breed  # Attribute to store breed
        self.age = age      # Attribute to store age
        self.color = color  # Attribute to store color

    # Method for the Dog class
    def bark(self):
        print(f"The {self.breed} is barking!")

    def sum_calc(self):
        print("fayas")

# Creating objects from the Dog class (instances of the class)
dog1 = Dog("Labrador", 3, "yellow")
dog1.bark()



# dog2 = Dog("Bulldog", 2, "white")

# # Accessing object attributes and methods
# print(dog1.breed)  # Output: Labrador
# dog2.bark()        # Output: The Bulldog is barking!
