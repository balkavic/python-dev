if False:

    pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
    }

    print(f"You ordered a {pizza['crust']}-crust pizza " 
          "with the following toppings:")

    for topping in pizza['toppings']:
        print(f"\t{topping}")

print("Which toppings would you like on your pizza?")
toppings = []
entered_topping = ""

while entered_topping != "quit":
    entered_topping = input("Enter your topping or 'quit' to finish: ")
    if entered_topping != "quit":
        print(f"Adding topping {entered_topping} to the pizza")
        toppings.append(entered_topping)

print("Ordered toppings: ")
print(toppings)
