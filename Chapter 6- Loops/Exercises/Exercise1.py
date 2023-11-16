pizza = "\nWhich pizza toppings are you in the mood for?"
pizza += "\nOnce you're done, enter 'quit': "

while True:
    topping = input(pizza)
    if topping != 'quit':
        print(f"  I'll top your pizza with {topping}.")
    else:
        break