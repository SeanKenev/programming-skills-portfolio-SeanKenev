rivers = {
    'Shinao': 'Japan',
    'Cagayan': 'Philippines',
    'Han': 'Korea',
    'Shannon': 'Ireland',
    'Laguna Grande': 'Puerto Rico',
    }

for river, country in rivers.items():
    print(f"The {river.title()} river travels through {country.title()}.")

print("\nThis data collection includes the following rivers:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThis data collection includes the following countries:")
for country in rivers.values():
    print(f"- {country.title()}")