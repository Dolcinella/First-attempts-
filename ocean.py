import random
from tkinter import *
from tkinter import ttk

from obstacle import Obstacle
from predator import Predator
from prey import Prey

# константы значений количества добычи, препятствий и хищников
NUM_OBSTACLES = 3
NUM_PREYS = 3
NUM_PREDATORS = 1


class Ocean:
    def __init__(self):
        self.__num_rows = 4
        self.__num_cols = 4
        self.__size = self.__num_cols * self.__num_rows
        self.__num_prey = NUM_OBSTACLES
        self.__num_obstacles = NUM_PREYS
        self.__random = random.randint(1, 5)
        self.__cells = [[None for i in range(self.__num_rows)] for j in range(self.__num_cols)]
        self.on_change = None

    def get_num_rows(self):  # Возвращает значение количества столбцов
        return self.__num_rows

    def get_num_cols(self):  # Возвращает значение количества колонок
        return self.__num_cols

    def display_cells_by_tink(self):  # Выводит состояне океана на экран в виде текста на кнопках
        for r in range(self.get_num_rows()):
            for c in range(self.get_num_cols()):
                btn = ttk.Button(text=f"{self.__cells[r][c]}")  # Создание кнопок для вывода текстовых значков
                btn.grid(row=r, column=c)  # вывод масива и размещение кнопок сеткой

    def check_object(self, x, y):
        mark = False
        if self.__num_rows > x > -1 and self.__num_cols > y > -1: # Проверка обьекта при движении, что он не выходит за рамки таблицы
            if self.__cells[x][y] is None: # Проверка является ли выбранная клетка свободной
                mark = True

        return mark

    def check_object_for_output(self, coord_1, coord_2):  # Проверка значения в иконке таблицы
        if self.__cells[coord_1][coord_2] is None:
            result = "oc"
        elif isinstance(self.__cells[coord_1][coord_2], Prey):
            result = "pry"
        elif isinstance(self.__cells[coord_1][coord_2], Obstacle):
            result = "ob"
        elif isinstance(self.__cells[coord_1][coord_2], Predator):
            result = "prd"

        return result

    def check_priorities_for_predator(self, x, y):  # создание приоритета хищника
        mark = False
        if self.__num_rows > x > -1 and self.__num_cols > y > -1:  # проверка не выходит ли выбранная клетка за рамки таблицы
            if isinstance(self.__cells[x][y], Prey):  # проверка обрабатываемой клетки на наличие добычи
                mark = True

        return mark

    def add_obstacles(self, quantity_obstacles=NUM_OBSTACLES):  # добавлене препятствий
        while quantity_obstacles > 0:
            x = random.randint(0, self.__num_rows - 1)  # рандомная координата х
            y = random.randint(0, self.__num_cols - 1)  # рандомная координата х
            if self.__cells[x][y] is None:  # проверка на свободность выбранной по координатам [x,y] клетки
                self.__cells[x][y] = Obstacle(x, y, self)  # помещение обьекта в выбранную клетку с координатами [x,y]
                quantity_obstacles -= 1

    def add_prey(self, quantity_prey=NUM_PREYS):  # добавлене добычи
        while quantity_prey > 0:
            x = random.randint(0, self.__num_rows - 1)  # рандомная координата х
            y = random.randint(0, self.__num_cols - 1)  # рандомная координата y
            if self.__cells[x][y] is None: # проверка на свободность выбранной по координатам [x,y] клетки
                self.__cells[x][y] = Prey(x, y, self) # помещение обьекта в выбранную клетку с координатами [x,y]
                quantity_prey -= 1

    def add_predator(self, quantity_prey=NUM_PREDATORS):  # добавлене хищников
        while quantity_prey > 0:
            x = random.randint(0, self.__num_rows - 1)  # рандомная координата х
            y = random.randint(0, self.__num_cols - 1)  # рандомная координата y
            if self.__cells[x][y] is None: # проверка на свободность выбранной по координатам [x,y] клетки
                self.__cells[x][y] = Predator(x, y, self) # помещение обьекта в выбранную клетку с координатами [x,y]
                quantity_prey -= 1

    def display_cells(self):  # отображение океана в консольном приложении
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                if self.__cells[i][j] is not None:
                    print(self.__cells[i][j], end=" ")
                else:
                    print("-", end=" ")
            print()

    def change_ocean(self, i, j):  # изменение океана
        if self.__cells[i][j] is not None:  # проверка на наличие обьекта класса Сells
            if self.__cells[i][j].get_status():  # проверка на повторную обработку
                moved_object = self.__cells[i][j]  # сдвигаемый обьект
                x, y = self.__cells[i][j].process()  # получения новых координат
                self.__cells[i][j] = None  # очищение старых координат
                self.__cells[x][y] = moved_object  # перемещение обьекта в новую позицию
            else:
                self.__cells[i][j].change_status()  # если обьект обрабатывается повторно, то меняем ему статус и пропускаем

    def get_data(self):  # Получение информации о количестве добычи, хищников и препятствий
        obstacle_quantity = 0
        prey_quantity = 0
        predator_quantity = 0
        for i in range(self.get_num_rows()):
            for j in range(self.get_num_rows()):
                if isinstance(self.__cells[i][j], Obstacle):
                    obstacle_quantity += 1
                elif isinstance(self.__cells[i][j], Prey):
                    prey_quantity += 1
                elif isinstance(self.__cells[i][j], Predator):
                    predator_quantity += 1

        return obstacle_quantity, prey_quantity, predator_quantity
