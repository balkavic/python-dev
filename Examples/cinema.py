end = False
ticket_price = 0

while not end:
    age = input("What is your age? "
                "(enter 'quit' to finish) ")
    if age != 'quit':
        if int(age) < 3:
            print("Move ticket is free under age of 3")
        elif int(age) < 13:
            print("Move ticket costs $10 between ages 3 and 12")
            ticket_price += 10
        else:
            print("Move ticket costs $15 above age of 12")
            ticket_price += 15
    else:
        end = True

print(f"Total cost of move ticket: ${ticket_price}")
