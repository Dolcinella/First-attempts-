from cell import Cell


class Obstacle(Cell):
    def __init__(self, i, j, owner):
        super().__init__(i, j, owner)
        self.__image = '#'
        self.__status = True

    def __str__(self):
        result = self.__image

        return result

    def get_status(self):  # получение статуса обьекта
        return self.__status

    def change_status(self): # изменение статуса обьекта
        if self.__status is True:
            self.__status = False
        elif self.__status is False:
            self.__status = True

    def process(self):  # действия обьекта при изменении океана
        coord = self.get_coordinate()
        return coord[0], coord[1]
