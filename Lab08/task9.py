from user import User
from admin import Admin


def task09a():
    user1 = User("Іван", "Петренко", "ivan@example.com", "ivan_p", True)
    user2 = User("Марія", "Коваленко", "maria@example.com", "maria_k", False)
    user3 = User("Олександр", "Сидоренко", email="alex@example.com", newsletter_subscription=True)

    users = [user1, user2, user3]
    for user in users:
        user.describe_user()
        user.greeting_user()
        print()


def task09b():
    user = User("Тестовий", "Користувач")
    
    print(f"Початкові спроби входу: {user.login_attempts}")
    
    user.increment_login_attempts()
    user.increment_login_attempts()
    user.increment_login_attempts()
    
    print(f"Спроби входу після збільшення: {user.login_attempts}")
    
    user.reset_login_attempts()
    print(f"Спроби входу після скидання: {user.login_attempts}")


def task09c():
    admin = Admin("Адміністратор", "Системи", "admin@example.com", "admin", True)
    admin.show_privileges()


def task09d():
    admin = Admin("Головний", "Адмін", "main_admin@example.com", "main_admin", True)
    admin.privileges.show_privileges()


def task09():
    task09a()
    task09b()
    task09c()
    task09d()


task09()

