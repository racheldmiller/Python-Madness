# Given a person variable:
# person = [["name", "Jared"], ["job", "Musician", ["city", "Bern"]]]
# Create a dictionary called answer, that makes each first item in the list a key and the second item a corresponding value.
# {'name': 'Jared, 'job': 'Musician', 'city': 'Bern'}

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

answer = {thing[0]: thing[1] for thing in person}

# OR
# answer = dict(person)
