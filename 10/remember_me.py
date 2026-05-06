import json


def get_stored_username():
    """Видобути збереженне ім'я, якщо таке є."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        if user == username:
            return username
        else:
            return None


def get_new_username():
    """Запитати ім'я користувача."""
    username = user
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Привітати користувача на ім'я"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We`ll remember you when you come back, {username}!")


guest = input("What is your username?")
user = guest.title()
greet_user()
