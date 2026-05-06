"""prompt = "Tell me something, and I will repeat it back to you "
prompt += "\nEnter 'quit' to end the program"
message = ''

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


name = input("Please enter your name: ")
print(f"\nHello, {name}")

promt = "If you tell us who you are, we can personalize massages you see."
promt += "\nWhat is your first name? "

name = input(promt)
print(f"\nHello, {name}")


age = input("How old are you? ")
age = int(age)
age <= 18
print(bool(age))


height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride! ")
else:
    print("\nYou'll be able to ride when you're a little older. ")


number = input("Enter a number, and I'll tell you id it's even or odd")
number = int(number)

if number %2 == 0:
    print(f"\nThe number {number} is even")
else:
    print(f"\nThe number {number} is odd")"""

"""prompt = "Tell me something, and I will repeat it back to you "
prompt += "\nEnter 'quit' to end the program"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)"""

"""prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")"""

"""unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)

print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())"""

"""pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)"""


responses = {}


polling_active = True

while polling_active:

    name = input("\nWhat is your name?")
    response = input("Which mountain you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes/no)")

    if repeat == 'no':
        polling_active = False

    print("\n----Poll Results----")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}")







