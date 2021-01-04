favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print(favorite_languages)

language = favorite_languages['sarah'].title()

friends = ['phil', 'sarah']

print(f"Sarah's favorite language is {language}")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages:
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages:
    print("Erin, please take your poll!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

rivers = {
    'nile': 'egypt',
    'danube': 'germany',
    'amazonas': 'brazil'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    wording_languages = 'languages are'
    if len(languages) == 1:
        wording_languages = 'language is'
    print(f"\n{name.title()}'s favorite {wording_languages}:")
    for language in languages:
        print(f"\t{language.title()}")
