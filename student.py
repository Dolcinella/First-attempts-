class Student:
    def __init__(self, name, family_name, student_id, email, *subjects_ids):
        self.__name = name
        self.__family_name = family_name
        self.__student_id = student_id
        self.__email = email

    def __str__(self):
        return f"Имя: {self.__name:10} Фамилия: {self.__family_name:10} ID: {self.__student_id:10} email: {self.__email}"

    def set_name(self, new_name):
        self.__name = new_name

    def set_family_name(self, new_name):
        self.__family_name = new_name

    def set_email(self, new_name):
        self.__email = new_name

    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def get_family_name(self):
        return self.__family_name

    def get_email(self):
        return self.__email
