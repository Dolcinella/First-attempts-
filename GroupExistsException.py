class GroupExistsException(Exception):
    def __str__(self):
        print("Такая группа уже существует")