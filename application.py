import time
from tkinter import PhotoImage, Tk, ttk, Toplevel, Label


class Application:
    def __init__(self, ocean):
        self.__ocean = ocean
        self.__root = Tk()  # создание окна Tkinter
        self.__buttons = []  # создание пустого масива для ячеек океана
        self.__entry = ttk.Entry()  # создание entry бокса для ввода количества итераций
        # создание ссылок на картинки, что применяются для вывода океана
        self.image1 = PhotoImage(file="ocean.png")
        self.image2 = PhotoImage(file="obstacle.png")
        self.image3 = PhotoImage(file="fish.png")
        self.image4 = PhotoImage(file="predator.png")

    def stop(self):  # функция остановки океана
        self.__root.destroy()

    def start_application(self):  # функция создания окна для вывода океана
        button2 = ttk.Button(text="Show Stats", command=self.show_info)  # создание кнопки для вывода
        button1 = ttk.Button(text="Next Step", command=self.a_few_next_steps)  # создание показа изменений в океане
        entry = self.__entry
        button3 = ttk.Button(text="Stop", command=self.stop)  # создание кнопки для остановки программы

        # размещение кнопок в океане
        button1.grid(row=self.__ocean.get_num_rows(), column=0)
        entry.grid(row=self.__ocean.get_num_rows(), column=1)
        button2.grid(row=self.__ocean.get_num_rows(), column=2)
        button3.grid(row=self.__ocean.get_num_rows(), column=3)

        # создание ячеек кнопок для вывода элементов океана
        for i in range(self.__ocean.get_num_rows()):
            self.__buttons.append([])
            for j in range(self.__ocean.get_num_cols()):
                # проверка обрабатываемого элемента океана для подвязкии к нему соответствующей картинки
                ocean_element = self.__ocean.check_object_for_output(i, j)
                # привязка картинки к кнопке
                if ocean_element == "oc":

                    btn = ttk.Button(image=self.image1)
                elif ocean_element == "ob":

                    btn = ttk.Button(image=self.image2)
                elif ocean_element == "pry":

                    btn = ttk.Button(image=self.image3)
                elif ocean_element == "prd":

                    btn = ttk.Button(image=self.image4)

                self.__buttons[i].append(btn)  # помещение данной кнопки в массив
                btn.grid(row=i, column=j)

        self.__root.mainloop()

    def a_few_next_steps(self):  # Функция для изменение океана в несколько итераций
        repeats_quantity = int(self.__entry.get())  # ввод количества итераций
        for i in range(repeats_quantity):
            self.next_step()  # изменение океана
            self.__root.update()  # обновление картинок на кнопках массива
            time.sleep(1)  # задержка для не моментального вывода конечного результата

    def next_step(self):  # Функция для изменение океана

        # Изменение океана
        for r in range(self.__ocean.get_num_rows()):
            for c in range(self.__ocean.get_num_cols()):
                self.__ocean.change_ocean(r, c)

        # привязка новых иизображений к кнопкам вывода океана
        for i in range(self.__ocean.get_num_rows()):
            for j in range(self.__ocean.get_num_cols()):
                ocean_element = self.__ocean.check_object_for_output(i, j)
                if ocean_element == "oc":

                    self.__buttons[i][j]["image"] = self.image1
                elif ocean_element == "ob":

                    self.__buttons[i][j]["image"] = self.image2
                elif ocean_element == "pry":

                    self.__buttons[i][j]["image"] = self.image3
                elif ocean_element == "prd":

                    self.__buttons[i][j]["image"] = self.image4

    def show_info(self):  # функция для вывода информации об обьектах океана
        stats_window = Toplevel(self.__root)  # вывод нового окна
        stats_window.title("Stats")  # создание заголовка
        stats_window.geometry("250x200")  # размер окна
        obstacle_quantity, prey_quantity, predator_quantity = self.__ocean.get_data()  # получение информации об обьектах океана
        lbl1 = Label(stats_window, text=f"Quantity of obstacles: {obstacle_quantity}")  # вывод количества препятствий
        lbl2 = Label(stats_window, text=f"Quantity of prey: {prey_quantity}")  # вывод количества добычи
        lbl3 = Label(stats_window, text=f"Quantity of predators: {predator_quantity}")  # вывод количества хищников
        lbl1.pack()
        lbl2.pack()
        lbl3.pack()
