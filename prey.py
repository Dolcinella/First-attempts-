import random
from cell import Cell


class Prey(Cell):
    def __init__(self, i, j, owner):
        super().__init__(i, j, owner)
        self.__image = 'f'
        self.__status = True

    def __str__(self):
        result = self.__image

        return result

    def get_status(self):  # получение статуса обьекта
        return self.__status

    def change_status(self):  # изменение статуса обьекта
        if self.__status is True:
            self.__status = False
        elif self.__status is False:
            self.__status = True

    def find_new_coord(self, x, y):  # поиск свободной ячейки для перемещения
        result = self.get_coordinate()
        west = [x - 1, y]
        east = [x + 1, y]
        north = [x, y + 1]
        south = [x, y - 1]
        # поиск свободных ячеек для перемещения
        possible_directions = [west, east, north, south]
        while len(possible_directions) > 0:
            random_position = random.randint(0, len(possible_directions) - 1)  # рандомный выбор обрабатываемого направления
            current_direction = possible_directions.pop(random_position)  # убираем обрабатываемое направление из списка возможных направлений
            if self._owner.check_object(current_direction[0], current_direction[1]):  # проверка является ли клетка свободной
                if current_direction == east or current_direction == north:  # если да, проверяем на сдвиг вправо и вниз
                    self.change_status()  # изменение статуса при перемещении вниз и вправо,
                    # что бы при повторной проверке обьекты не перемещались
                result = current_direction
                break

        return result

    def process(self):  # действия обьекта при изменении океана
        coord = self.get_coordinate()  # получение базовых координат обьекта
        new_coord = self.find_new_coord(coord[0], coord[1])  # получение новых координат обьекта
        if new_coord is not None:  # проверка сдвинулся ли обьект
            self.set_coordinate(new_coord)  # перемещение обьекта в новую ячейку

        return new_coord[0], new_coord[1]




