class Restaurant:
    """"Завдання 9-1, 9-4, 9-6"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name.title()}")
        print(f"Restaurant cuisine type is {self.type}")

    def open_restaurant(self):
        print(f"{self.name.title()} is open now")

    def read_number_served(self):
        print(f"The current number of served clients is {self.number_served}")

    def set_number_served(self, count):
        if count >= self.number_served:
            self.number_served = count
        else:
            print("Not possible")

    def increment_number_served(self, count):
        self.number_served += count


class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name, cuisine_type, flavours='vanile'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavs = flavours

    def icecream_flavours(self):
        print(f"You have icecream with {self.flavs}")



