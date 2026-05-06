
ingredients = "\nWhat ingredients you wanna to add to your pizza?"
ingredients += "\n(If you wanna to stop print 'quit')"

while True:
    pizza = input(ingredients)

    if pizza == 'quit':
        break
    else:
        print(f"Id like to take pizza with{pizza} ")

