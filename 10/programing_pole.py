filename = 'answers.txt'

print("If you want to close the program enter 'quit'")

with open(filename, 'w') as file_object:
    while True:
        question = input("Why do you like the programing:")
        if question == 'quit':
            break
        else:
            file_object.write(f"{question.title()}\n")