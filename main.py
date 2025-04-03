from animal import Animal
from dog import Dog

if __name__ == "__main__":

    bird = Animal("Big Bird", "YellowFeather")
    print(bird)
    bird.speak()

    fido = Dog("Fido", "Canine", "Hound")
    print(fido)
    fido.speak()

    print("All Animals:")
    # TODO print out all the animals

    animals = Animal.get_all_animals()
    for animal in animals:
        print(animal)