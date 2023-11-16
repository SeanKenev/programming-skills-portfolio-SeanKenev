sandwich_orders = [
    'pastrami', 'philly cheesesteak', 'nashville hot chicken', 'pastrami',
    'rueben', 'meatball sub', 'pastrami']
finished_sandwiches = []

print("Apologies, but we don't have any pastrami available today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm preparing your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I assembled a {sandwich} sandwich.")