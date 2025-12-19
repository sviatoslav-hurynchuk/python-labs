class User:
    def __init__(self, first_name, last_name, email="", nickname="", newsletter_subscription=False):
        if not isinstance(first_name, str) or not first_name.strip():
            self.valid = False
            self.first_name = None
            self.last_name = None
            self.email = ""
            self.nickname = ""
            self.newsletter_subscription = False
            self.login_attempts = 0
            return
        
        if not isinstance(last_name, str) or not last_name.strip():
            self.valid = False
            self.first_name = None
            self.last_name = None
            self.email = ""
            self.nickname = ""
            self.newsletter_subscription = False
            self.login_attempts = 0
            return
        
        self.valid = True
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        
        if email:
            if not isinstance(email, str):
                self.valid = False
                self.email = ""
                return
            if "@" not in email or "." not in email.split("@")[-1]:
                self.valid = False
                self.email = ""
                return
        self.email = email.strip() if email else ""
        
        if nickname:
            if not isinstance(nickname, str):
                self.valid = False
                self.nickname = ""
                return
            if len(nickname) > 50:
                self.valid = False
                self.nickname = ""
                return
        self.nickname = nickname.strip() if nickname else ""
        
        if not isinstance(newsletter_subscription, bool):
            self.valid = False
            self.newsletter_subscription = False
        else:
            self.newsletter_subscription = newsletter_subscription
        
        self.login_attempts = 0
    
    def describe_user(self):
        if not self.valid:
            return None
        
        lines = [f"Повне ім'я: {self.first_name} {self.last_name}"]
        if self.email:
            lines.append(f"Поштова адреса: {self.email}")
        if self.nickname:
            lines.append(f"Нікнейм: {self.nickname}")
        lines.append(f"Розсилка новин: {'Так' if self.newsletter_subscription else 'Ні'}")
        
        return "\n".join(lines)
    
    def greeting_user(self):
        if not self.valid:
            return None
        return f"Привіт, {self.first_name} {self.last_name}! Раді вас бачити на сайті."
    
    def increment_login_attempts(self):
        if not self.valid:
            return
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        if not self.valid:
            return
        self.login_attempts = 0


class Privileges:
    def __init__(self):
        self.privileges = [
            "Allowed to add message",
            "Allowed to delete users",
            "Allowed to ban users",
        ]
    
    def show_privileges(self):
        lines = ["Привілеї адміністратора:"]
        for privilege in self.privileges:
            lines.append(f"  - {privilege}")
        return "\n".join(lines)


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
        if not self.valid:
            return None
        
        lines = ["Привілеї адміністратора:"]
        for privilege in self.privileges_list:
            lines.append(f"  - {privilege}")
        return "\n".join(lines)

