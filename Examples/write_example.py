filename = 'guest.txt'

with open(filename, 'w') as file_object:
    while True:
        name = input("Give me your name ('quit' to end): ")
        if name == 'quit':
            break
        print(f"Welcome, {name}!")
        file_object.write(f"{name}\n")
