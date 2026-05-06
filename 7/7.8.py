
sandwich_orders = ['burgher', 'cheeseburgher', 'club sandwich', 'submarine sandwich', 'open sandwich', 'pocket sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made your {current_sandwich}')

    finished_sandwiches.append(current_sandwich)

print("Finished sandwiches are:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
