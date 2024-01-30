class IncorrectStudentIDException(Exception):
    def __str__(self):
        return "Студенческий ID введен не верно, такого студента не существует"
