def make_shirt(size='large', message='I love Python!'):
    """A brief description of the expected shirt."""
    print("\nI'll be creating a " + size + " coding shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Oh shift!')