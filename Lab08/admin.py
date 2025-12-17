from user import User


class Privileges:
    def __init__(self):
        self.privileges = [
            "Allowed to add message",
            "Allowed to delete users",
            "Allowed to ban users",
        ]

    def show_privileges(self):
        print("Привілеї адміністратора:")
        for privilege in self.privileges:
            print(f"  - {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, email="", nickname="", newsletter_subscription=False):
        super().__init__(first_name, last_name, email, nickname, newsletter_subscription)
        self.privileges_list = [
            "Allowed to add message",
            "Allowed to delete users",
            "Allowed to ban users",
        ]
        self.privileges = Privileges()

    def show_privileges(self):
        print("Привілеї адміністратора:")
        for privilege in self.privileges_list:
            print(f"  - {privilege}")

