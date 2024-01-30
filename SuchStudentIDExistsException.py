class SuchStudentIDExistsException(Exception):
    def __str__(self):
        print("Это ID присвоено другому студенту группы")