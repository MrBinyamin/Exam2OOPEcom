from bonus.Cat import Cat
from bonus.Fish import Fish
from bonus.Pet import Pet
from bonus.Spider import Spider

print("--- Testing Spider ---")
spider = Spider()
spider.walk()  # Inherited from Animal (8 legs)
spider.eat()  # Implemented in Spider

# 2. Testing Cat (inherits Animal, implements Pet)
print("\n--- Testing Cat ---")
cat1 = Cat("Tom")
print(f"Cat's name is: {cat1.get_name()}")
cat1.walk()  # Inherited from Animal (4 legs)
cat1.play()  # Implemented from Pet
cat1.eat()  # Implemented in Cat

# Testing the setter and default constructor
cat1.set_name("Garfield")
print(f"Cat's new name is: {cat1.get_name()}")

cat2 = Cat()  # Default constructor (empty name)
print(f"Unnamed cat's name is: '{cat2.get_name()}'")

# 3. Testing Fish (inherits Animal, implements Pet)
print("\n--- Testing Fish ---")
fish = Fish()
fish.set_name("Nemo")
print(f"Fish's name is: {fish.get_name()}")
fish.walk()  # Overridden in Fish (0 legs, cannot walk)
fish.play()  # Implemented from Pet
fish.eat()  # Implemented in Fish

# 4. Testing Polymorphism
print("\n--- Testing Polymorphism (List of Animals) ---")
animals = [Spider(), Cat("Luna"), Fish()]

for animal in animals:
    # We can call walk() and eat() safely because they are defined in the Animal base class
    print(f"\nLooking at a {animal.__class__.__name__}:")
    animal.walk()
    animal.eat()

    # We can also check if the animal is a Pet (implements the Pet interface)
    if isinstance(animal, Pet):
        print(f"This is a pet. Let's play with {animal.get_name()}!")
        animal.play()