from student import Student


class Group_UI:

    def input_student_UI(self):
        # choice = 1
        name = str(input("Введите имя нового студента : "))
        surname = str(input("Введите фамилию студента : "))
        student_id = str(input("Введите ID студента : "))
        email = str(input("Введите имейл студента : "))
        student = [name, surname, student_id, email]
        # choice = int(input("Продолжить добавление - 1; \n Завершить добавление - 2; \n Ваш выбор: "))

        return student

    def make_choice(self):
        choice = int(input("Продолжить добавление - 1; \n Завершить добавление - 2; \n Ваш выбор: "))

        return choice

    def input_file_name(self):
        file_name = input("Введите имя файла")

        return file_name

    def input_student_ID(self):
        student_ID = input("Введите ID студента")

        return student_ID

    def input_new_name(self):
        new_name = input("Введите новое: ")

        return new_name

    def choose_parameter(self):
        choice = int(input("Что вы хотите поменять? \n Имя - 1\n Фамилия - 2 \n Почта - 3 \n"))

        return choice