from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, stand_name, stand_type, flavors):
        super().__init__(stand_name, stand_type)
        self.flavors = flavors

    def describe_restaurant(self):
        print(f"Ice cream stand {self.name} is a(n) {self.cuisine_type} stand, with flavors {', '.join(self.flavors)}")

my_ice_cream_stand = IceCreamStand("Bazsi's place", "Italian", ["vanilla", "chocolate", "strawberry"])

my_ice_cream_stand.describe_restaurant()
