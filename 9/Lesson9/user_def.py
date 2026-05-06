from User import User
from admin import Admin


user_1 = User('Alex', 'Smith', 21, 'alexsmith0002@gmail.com')
user_2 = User('Kobe', 'Bryant', 35, 'blackmamba@gmail.com')
user_3 = User('Lebron', 'James', 95, 'theking@gmail.com')
user_4 = User('Paul', 'Gasol', 43, 'paulgas@gmail.com')
user_5 = Admin('Jotaro', 'Jovani', 26, 'jojo@gmail.com')

user_1.describe_user()
user_2.describe_user()
user_3.describe_user()
user_4.describe_user()

user_1.greet_user()
user_2.greet_user()
user_3.greet_user()
user_4.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)

user_5.describe_user()
user_5.privileges.show_privileges()
