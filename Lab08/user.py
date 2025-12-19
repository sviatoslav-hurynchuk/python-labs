class User:
    def __init__(self, first_name, last_name, email="", nickname="", newsletter_subscription=False):
        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError("Ім'я має бути непустим рядком")
        if not isinstance(last_name, str) or not last_name.strip():
            raise ValueError("Прізвище має бути непустим рядком")
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()

        if email:
            if not isinstance(email, str):
                raise ValueError("Email має бути рядком")
            if "@" not in email or "." not in email.split("@")[-1]:
                raise ValueError("Невірний формат email")
        self.email = email.strip() if email else ""

        if nickname:
            if not isinstance(nickname, str):
                raise ValueError("Нікнейм має бути рядком")
            if len(nickname) > 50:
                raise ValueError("Нікнейм занадто довгий")
        self.nickname = nickname.strip() if nickname else ""

        if not isinstance(newsletter_subscription, bool):
            raise ValueError("newsletter_subscription має бути булевим значенням")
        self.newsletter_subscription = newsletter_subscription
        self.login_attempts = 0

    def describe_user(self):
        print(f"Повне ім'я: {self.first_name} {self.last_name}")
        if self.email:
            print(f"Поштова адреса: {self.email}")
        if self.nickname:
            print(f"Нікнейм: {self.nickname}")
        print(f"Розсилка новин: {'Так' if self.newsletter_subscription else 'Ні'}")

    def greeting_user(self):
        print(f"Привіт, {self.first_name} {self.last_name}! Раді вас бачити на сайті.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

