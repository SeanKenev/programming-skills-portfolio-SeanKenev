ticket = "\nAt what age are you?"
ticket += "\nOnce you're done, enter 'quit': "

while True:
    age = input(ticket)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  Toddlers can enter free of charge.")
    elif age < 13:
        print("  It is 10 dollars for your movie ticket.")
    else:
        print("  It is 15 dollars for your ticket.")