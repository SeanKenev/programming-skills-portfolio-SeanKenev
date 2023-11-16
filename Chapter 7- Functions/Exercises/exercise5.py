def describe_city(city, country='Japan'):
    """Locating a city."""
    msg = city.title() + " is located in " + country.title() + "."
    print(msg)

describe_city('Tokyo')
describe_city('Seoul', 'Korea')
describe_city('Nagoya')