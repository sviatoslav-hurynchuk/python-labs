from lab8_task9 import User, Admin, Privileges


class TestUser:
    def test_task09a_create_instance_and_attributes(self):
        user = User("Іван", "Петренко", "ivan@example.com", "ivan_p", True)
        
        assert user.first_name == "Іван"
        assert user.last_name == "Петренко"
        assert user.email == "ivan@example.com"
        assert user.nickname == "ivan_p"
        assert user.newsletter_subscription is True
    
    def test_task09a_describe_user(self):
        user = User("Іван", "Петренко", "ivan@example.com", "ivan_p", True)
        
        output = user.describe_user()
        
        assert output is not None
        assert "Іван" in output
        assert "Петренко" in output
        assert "ivan@example.com" in output
        assert "ivan_p" in output
    
    def test_task09a_greeting_user(self):
        user = User("Іван", "Петренко", "ivan@example.com", "ivan_p", True)
        
        output = user.greeting_user()
        
        assert output is not None
        assert "Іван" in output
        assert "Петренко" in output
        assert "Привіт" in output
    
    def test_task09a_multiple_users(self):
        user1 = User("Іван", "Петренко", "ivan@example.com", "ivan_p", True)
        user2 = User("Марія", "Коваленко", "maria@example.com", "maria_k", False)
        user3 = User("Олександр", "Сидоренко", email="alex@example.com", newsletter_subscription=True)
        
        assert user1.first_name == "Іван"
        assert user2.first_name == "Марія"
        assert user3.first_name == "Олександр"
        
        output1 = user1.describe_user()
        output2 = user1.greeting_user()
        assert "Іван" in output1
        assert "Іван" in output2
        
        output3 = user2.describe_user()
        output4 = user2.greeting_user()
        assert "Марія" in output3
        assert "Марія" in output4
    
    def test_task09b_login_attempts_default(self):
        user = User("Тестовий", "Користувач")
        assert user.login_attempts == 0
    
    def test_task09b_increment_login_attempts(self):
        user = User("Тестовий", "Користувач")
        
        user.increment_login_attempts()
        assert user.login_attempts == 1
        
        user.increment_login_attempts()
        assert user.login_attempts == 2
        
        user.increment_login_attempts()
        assert user.login_attempts == 3
    
    def test_task09b_reset_login_attempts(self):
        user = User("Тестовий", "Користувач")
        
        user.increment_login_attempts()
        user.increment_login_attempts()
        user.increment_login_attempts()
        assert user.login_attempts == 3
        
        user.reset_login_attempts()
        assert user.login_attempts == 0


class TestAdmin:
    def test_task09c_inheritance(self):
        admin = Admin("Адміністратор", "Системи", "admin@example.com", "admin", True)
        assert isinstance(admin, User)
        assert admin.first_name == "Адміністратор"
        assert admin.last_name == "Системи"
    
    def test_task09c_privileges_attribute(self):
        admin = Admin("Адміністратор", "Системи", "admin@example.com", "admin", True)
        assert hasattr(admin, 'privileges_list')
        assert isinstance(admin.privileges_list, list)
        assert "Allowed to add message" in admin.privileges_list
        assert "Allowed to delete users" in admin.privileges_list
        assert "Allowed to ban users" in admin.privileges_list
    
    def test_task09c_show_privileges(self):
        admin = Admin("Адміністратор", "Системи", "admin@example.com", "admin", True)
        
        output = admin.show_privileges()
        
        assert output is not None
        assert "Привілеї адміністратора" in output
        assert "Allowed to add message" in output
        assert "Allowed to delete users" in output
        assert "Allowed to ban users" in output
    
    def test_task09d_privileges_class(self):
        admin = Admin("Головний", "Адмін", "main_admin@example.com", "main_admin", True)
        assert hasattr(admin, 'privileges')
        assert isinstance(admin.privileges, Privileges)
    
    def test_task09d_privileges_show_privileges(self):
        admin = Admin("Головний", "Адмін", "main_admin@example.com", "main_admin", True)
        
        output = admin.privileges.show_privileges()
        
        assert output is not None
        assert "Привілеї адміністратора" in output
        assert "Allowed to add message" in output
        assert "Allowed to delete users" in output
        assert "Allowed to ban users" in output
    
    def test_task09e_import_and_use(self):
        admin = Admin("Тестовий", "Адмін", "test@example.com", "test_admin", False)
        
        output = admin.privileges.show_privileges()
        
        assert output is not None
        assert "Привілеї адміністратора" in output
        assert "Allowed to add message" in output
        assert "Allowed to delete users" in output
        assert "Allowed to ban users" in output


def task02():
    import pytest
    pytest.main([__file__, '-v'])


task02()

