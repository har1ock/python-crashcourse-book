filename = 'guest_name.txt'

print("Якщо ви хочете вийти з програми введіть 'quit'")


with open(filename, 'w') as file_object:
    while True:
        name = input("Введіть ваше ім'я:")

        if name == 'quit':
            break
        else:
            print(f"Hi {name.title()} great to see you")
            file_object.write(f"{name.title()} arrived \n")

