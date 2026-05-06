class Dog:
    """"Проста спроба змоделювати собаку """

    def __init__(self, name, age):
        """"Ініціювати атрибути ім'я та вік."""
        self.name = name
        self.age = age

    def sit(self):
        """"Симулювання виконання команди 'сидіти'."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """"Симулювання виконання команди 'лежати'."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

