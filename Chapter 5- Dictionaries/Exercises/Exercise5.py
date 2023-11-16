pets = []

pet = {
    'Animal': 'Hermit Crab',
    'Name': 'Krakatoa',
    'Pet owner': 'Dwayne',
    'Weight': 2,
    'Food': 'Mealworms',
}
pets.append(pet)

pet = {
    'Animal': 'Rabbit',
    'Name': 'Cookies',
    'Pet owner': 'Jonn',
    'Weight': 12,
    'Food': 'Vegetables',
}
pets.append(pet)

pet = {
    'Animal': 'Bird',
    'Name': 'Lemon',
    'Pet owner': 'Cailey',
    'Weight': 3,
    'Food': 'Seeds and Fruits',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I'm aware of {pet['Name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")