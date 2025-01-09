# Задача:
# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.

# Обозначение родительского класса User и его атрибутов
class User():
    def __init__(self, user_id, name):
        self._user_id = user_id         # Атрибут ID
        self._name = name               # Атрибут имя
        self._level = "user"            # Атрибут уровня доступа

    def get_user_id(self):
        return self._user_id            # Метод получения id пользователя (уровень доступа "защищенный")

    def get_name(self):
        return self._name               # Метод получения имени пользователя (уровень доступа "защищенный")

    def get_level(self):
        return self._level              # Метод получения уровня доступа пользователя (уровень доступа "защищенный")

    def set_name(self, name):
        self._name = name               # Метод изменения имени пользователя
        return self._name

# Обозначение класса Admin (производного от User) и его атрибутов
class Admin(User):
    def __init__(self, user_id, name):      # Метод инициализации атрибутов класса
        super().__init__(user_id, name)     # Метод инициализации атрибутов родительского класса
        self._level = "admin"               # Новый атрибут производного класса

    def add_user(self, user_list, user):
        user_list.append(user)              # Добавляем пользователя в список
        print(f"\nПользователь {user.get_name()} успешно добавлен в список.")
        self.display_user_list(user_list)   # Выводим актуальный список пользователей

    def remove_user(self, user_list, user):
        if user in user_list:
            user_list.remove(user)          # Удаляем пользователя из списка
            print(f"\nПользователь {user.get_name()} успешно удален из списка.")
        else:
            print(f"\nОшибка: пользователь {user.get_name()} не найден в списке.")
        self.display_user_list(user_list)   # Выводим актуальный список пользователей

    def display_user_list(self, user_list):                     # Определение метода вывода списка пользователей класса         print("\nАктуальный список пользователей:")             # Выводим актуальный список пользователей
        if not user_list:                                       # При отсутствии пользователей в списке
            print("Список пользователей пуст")
        else:
            for idx, user in enumerate(user_list, start=1):     # Циклический просмотр индексов в списке, начиная с 1-го
                print(f"{idx}. ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_level()}")

# Создание объектов классов
user_list = []
admin = Admin("a1", "Гоша")
user1 = User("u1", "Степа%")
user2 = User("u2", "Вася")
user3 = User("u3", "Коля")

# Тестирование методов классов
print(user1.get_name())            # Выводим имя пользователя user1
print(user1.set_name("Степа"))     # Переименовываем пользователя и сразу выводим новое имя

admin.add_user(user_list, user1)
admin.add_user(user_list, user2)
admin.add_user(user_list, user3)
admin.remove_user(user_list, user3)



