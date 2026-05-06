import json


def get_number():
    """Видобути збережене число """
    filename = 'favnumber.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        if digit == number:
            return number
        else:
            return None



def new_number():
    """"Ввести нове число в файл"""
    filename = 'favnumber.json'
    number = digit
    with open(filename, 'w') as f:
        json.dump(number, f)
    return number


def declare_a_number():
    number = get_number()
    if number:
        print(f"Your favorite number is {number}")
    else:
        number = new_number()
        print(f"Your new favorite number is {number}")


try:
    digit = int(input("What is your favorite number?"))
except ValueError:
    print("Please enter the number")


declare_a_number()
