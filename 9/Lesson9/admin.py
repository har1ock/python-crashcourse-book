from User import User


class Privileges:

    def __init__(self, privileges='delete post, ban people'):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Admin can: {self.privileges}")


class Admin(User):
    def __init__(self, first_name, last_name, person_age, e_mail):
        super().__init__(first_name, last_name, person_age, e_mail)
        self.privileges = Privileges()
