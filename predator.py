import random

from cell import Cell


class Predator(Cell):
    def __init__(self, i, j, owner):
        super().__init__(i, j, owner)
        self.__image = 'p'
        self.__status = True

    def __str__(self):
        result = self.__image

        return result

    def get_status(self):  # получене статуса
        return self.__status

    def change_status(self):  # изменение статуса
        if self.__status is True:
            self.__status = False
        elif self.__status is False:
            self.__status = True

    # find_new_coord - поиск ячейки для перемещения
    # arguments:
    #     x - x coordinate of object
    #     y - y coordinate of object
    # fields: _owner, ...
    # return: new coordinates
    # exceptions: ...
    def find_new_coord(self, x, y):
        result = self.get_coordinate()  # получение базовых координат обьекта
        west = [x - 1, y]
        east = [x + 1, y]
        north = [x, y + 1]
        south = [x, y - 1]
        possible_directions = [west, east, north, south]  # список возможных направлений для перемещения
        # блок проверки наличия приоритетов(добычи в соседних клетках) для хищника
        if self._owner.check_priorities_for_predator(west[0], west[1]):
            result = west
        elif self._owner.check_priorities_for_predator(east[0], east[1]):
            result = east
        elif self._owner.check_priorities_for_predator(north[0], north[1]):
            result = north
            self.change_status()
        elif self._owner.check_priorities_for_predator(south[0], south[1]):
            result = south
            self.change_status()
        else:
            # в противном случае поиск свободных ячеек для перемещения
            while len(possible_directions) > 0:
                random_position = random.randint(0, len(possible_directions) - 1)   # рандомный выбор обрабатываемого направления
                current_direction = possible_directions.pop(random_position)  # убираем обрабатываемое направление из списка возможных направлений
                if self._owner.check_object(current_direction[0], current_direction[1]):  # проверка является ли клетка свободной
                    if current_direction == east or current_direction == north:  # если да, проверяем на сдвиг вправо и вниз
                        self.change_status()  # если здвиг вправо или вниз меняем статус
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