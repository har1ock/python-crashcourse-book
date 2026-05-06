
inf = "\nWhat is your age"
inf += "\n(Enter 'quit' to end the program :"
active = True
while True:
    age = input(inf)
    age = int(age)
    if age < 3:
        print("Your ticket if free")
    elif age < 12:
        print("Your ticket cost 10$")
    elif age > 12:
        print("Your ticket cost 15$")
    elif age == 'quit':
        break


