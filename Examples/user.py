class User:
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.user_group = "user"
        self.login_attempts = 0

    def describe_user(self):
        print(f"User name: "
              f"{self.first_name} {self.last_name} ".title() +
              f"Email address: {self.email_address} "
              f"User group: {self.user_group} ")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}".title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self, privileges):
        """Represents user privileges."""
        self.privileges = privileges

    def describe_privileges(self):
        """Describe user's privileges."""
        print("User has the following privilieges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, email_address):
        super().__init__(first_name, last_name, email_address)
        self.user_group = "admin"
        self.privileges = Privileges(["can add posts", "can delete post", "can ban user"])

    def show_privileges(self):
        self.privileges.describe_privileges()

user1 = User("Bill", "Wake", "bill.wake@yahoo.com")
user2 = User("Jen", "Smith", "jen.smith@gmail.com")

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

admin_user = Admin("Rita", "Brown", "rita.brown@gmail.com")

admin_user.describe_user()
admin_user.show_privileges()

