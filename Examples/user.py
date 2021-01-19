class User:
    def __init__(self, first_name, last_name, email_address, user_group):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.user_group = user_group
        self.login_attempts = 0

    def describe_user(self):
        print(f"User name: "
              f"{self.first_name} {self.last_name} ".title() +
              f"Email address: {self.email_address} "
              f"User group: {self.user_group}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}".title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Bill", "Wake", "bill.wake@yahoo.com", "admin")
user2 = User("Jen", "Smith", "jen.smith@gmail.com", "user")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"User1 login attempts: {user1.login_attempts}")

user1.reset_login_attempts()

print(f"User1 login attempts: {user1.login_attempts}")
