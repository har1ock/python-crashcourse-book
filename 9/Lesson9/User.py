class User:
    """"Завдання 9-3, 9-5, 9-7"""
    def __init__(self, first_name, last_name, persons_age, e_mail):
        self.name = first_name
        self.surname = last_name
        self.age = persons_age
        self.mail = e_mail
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user first name is {self.name.title()}")
        print(f"The user last name is {self.surname.title()}")
        print(f"User have {self.age} years old")
        print(f"The users e-mail is {self.mail}")

    def greet_user(self):
        print(f"Happy to see you again {self.name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
