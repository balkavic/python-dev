class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant '{self.name}' is a(n) '{self.cuisine_type}' restaurant")

    def open_restaurant(self):
        print(f"{self.name} is now open.")

    def set_number_served(self, new_number_served):
        self.number_served = new_number_served

    def increment_number_served(self, served_increment):
        self.number_served += served_increment

my_restaurant = Restaurant("My Italian restaurant", "Italian")

print(my_restaurant.name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()

my_restaurant.open_restaurant()

your_restaurant = Restaurant("Your Mexican restaurant", "Mexican")

his_restaurant = Restaurant("His Indian restaurant", "Indian")


your_restaurant.describe_restaurant()

his_restaurant.describe_restaurant()

print(f"Served: {my_restaurant.number_served}")
my_restaurant.number_served += 1
print(f"Served: {my_restaurant.number_served}")

my_restaurant.set_number_served(5)

print(f"Served: {my_restaurant.number_served}")

my_restaurant.increment_number_served(10)

print(f"Served: {my_restaurant.number_served}")
