from name_function import get_formatted_name as fm

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = fm(first, last)
    print(f"\tNeatly formated name: {formatted_name}")