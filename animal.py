class Animal:
    
    """
    Base class representing a generic animal.
    """
    # Class-level attribute
    kingdom = "Animalia"
    all_animals = []

    # TODO create a class-level attribute that is a list of all the Animal objects
    def __init__(self, name, species):
        self.name = name
        self.species = species
    # TODO create the initializer for Animal with name and species as attributs
        Animal.all_animals.append(self)
    # TODO: Add a method to make a generic sound 
    def speak(self):
        print("The animal makes a noise.")
    # Call the method `speak` and make it output a specific message like 
    # "The animal makes a noise.""
    def __str__(self):
        return f"Kingdom: {self.kingdom}, Name: {self.name}, Species: {self.species}"

    # TODO __str__ method for string representation
    @classmethod
    def get_all_animals(cls):
        return cls.all_animals
    # Example output
    # Kingdom: 'kingdom attribute', Name: 'name attribute' Species: 'species attribute' 
