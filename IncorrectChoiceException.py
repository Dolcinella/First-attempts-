class IncorrectChoiceException(Exception):
    def __str__(self):
        print("Некорректный выбор")