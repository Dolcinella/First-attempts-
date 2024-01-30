class IncorrectGroupNumberException(Exception):
    def __str__(self):
        print("Данное значение группы введено не верно,введите целое число")