sandwich_orders = ['reuben', 'philly cheesesteak', 'nashville hot chicken', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm preparing your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I assembled a {sandwich} sandwich.")