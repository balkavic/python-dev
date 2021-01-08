def get_formatted_name(first_name, last_name):
    """"Return the full name, fully formatted."""
    return f"{first_name} {last_name}".title()

def build_person(first_name, last_name, age=None):
    """"Return a dictionaly of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

print(get_formatted_name("jimi", "hendrix"))

musician = build_person("jimi", "hendrix", 27)

print(musician)
