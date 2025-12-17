from admin import Admin


def task09e():
    admin = Admin("Тестовий", "Адміністратор", "test_admin@example.com", "test_admin", True)
    admin.privileges.show_privileges()


task09e()

