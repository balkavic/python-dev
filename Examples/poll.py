filename = 'programming_reasons.txt'

while True:
    reason = input("Why do you like programming? ('quit' to end)")
    if reason == "quit":
        break
    with open(filename, 'a') as file_object:
        file_object.write(reason + "\n")

