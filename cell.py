from random import random


class Cell():
    def __init__(self, i, j, owner):
        self.__coordinate = [i, j]
        self.__image = "-"
        self._owner = owner

    def get_coordinate(self):  # получене координаты
        return self.__coordinate

    def set_coordinate(self, coord):  # изменение координаты
        self.__coordinate = coord

    def process(self):  # действия обьекта при изменении океана
        pass



