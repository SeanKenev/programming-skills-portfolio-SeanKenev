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

