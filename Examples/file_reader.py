filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    # contents = file_object.read()
    # for line in file_object:
    #     print(line.rstrip())
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    # print(line.rstrip())
    pi_string += line.strip()

print(f"{pi_string[:102]}...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
    print(pi_string.find(birthday))
else:
    print("Your birthday does not appear in the first million digits of pi.")

# print(contents.rstrip())
