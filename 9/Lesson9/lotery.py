from random import choice

symbol = ['a', 'b', 'c', 'x', 'y', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
my_ticket = 'y'
cycle = 0
chosen_symbol = choice(symbol)
while chosen_symbol != my_ticket:
    chosen_symbol = choice(symbol)
    print(f"Wins {chosen_symbol} ticket, better luck next time")
    cycle = cycle + 1

else:
    print(f"You finally win, you only need {cycle} tries")
