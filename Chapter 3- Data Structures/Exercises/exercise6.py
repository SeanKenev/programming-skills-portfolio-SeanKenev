dguests = ['Andy Burnedead', 'Jack Hanses', 'Eva Mina', 'Fuuka Ayase']

name = dguests[0].title()
print(f"{name}, Please join us for dinner.")

name = dguests[1].title()
print(f"{name}, Please join us for dinner.")

name = dguests[2].title()
print(f"{name}, Please join us for dinner.")

name = dguests[3].title()
print(f"{name}, Please join us for dinner.")

name = dguests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

del(dguests[1])
dguests.insert(1, 'Eren Hunter')

name = dguests[0].title()
print(f"{name}, Please join us for dinner.")

name = dguests[1].title()
print(f"{name}, Please join us for dinner.")

name = dguests[2].title()
print(f"{name}, Please join us for dinner.")

name = dguests[3].title()
print(f"{name}, Please join us for dinner.")

print("\nWe got a bigger table!")
dguests.insert(0, 'Glarissa Ford')
dguests.insert(1, 'Julius Biscuit')
dguests.insert(2, 'Oliva Hammer')
dguests.append('Ymir James')

name = dguests[0].title()
print(name + ", Please join us for dinner.")

name = dguests[1].title()
print(name + ", Please join us for dinner.")

name = dguests[2].title()
print(name + ", Please join us for dinner.")

name = dguests[3].title()
print(name + ", Please join us for dinner.")

name = dguests[4].title()
print(name + ", Please join us for dinner.")

name = dguests[5].title()
print(name + ", Please join us for dinner.")

print("\nSorry, we can only invite two people to dinner.")

name = dguests.pop()
print("Sorry, " + name.title() + " There isn't any space at the table.")

name = dguests.pop()
print("Sorry, " + name.title() + " There isn't any space at the table.")

name = dguests.pop()
print("Sorry, " + name.title() + " There isn't any space at the table.")

name = dguests.pop()
print("Sorry, " + name.title() + " There isn't any space at the table.")

name = dguests.pop()
print("Sorry, " + name.title() + " There isn't any space at the table.")

name = dguests[0].title()
print(name + ", Please join us for dinner.")

name = dguests[1].title()
print(name + ", Please join us for dinner.")

name = dguests[2].title()
print(name + ", Please join us for dinner.")

del(dguests[0])
del(dguests[0])
del(dguests[0])

print(dguests)