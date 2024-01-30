import csv
from functools import partial
from tkinter import *
from tkinter.ttk import *

from group import Group


class Tk_Interface:
    def __init__(self, faculty_name="philology"):
        self.__groups_list = None
        self.__chosen_faculty = faculty_name
        self.__main_window = Tk()
        self.__chosen_group = None
        self.__groups_of_faculty = None
        self.__students_table = None
        self.__actions = None

    def change_data(self):
        variant = self.__actions.get()
        if variant == "Удалить студента":
            self.input_deleted_student()
        else:
            self.input_new_student()

    def create_main_window(self):
        self.__main_window.title("База даних")
        self.__main_window.geometry("800x500")

        label1 = Label(self.__main_window, text="Cписок групп факультета:")
        label2 = Label(self.__main_window, text="Cписок студентов выбранной групы:")
        label3 = Label(self.__main_window, text="Возможные действия:")
        label1.place(x=5, y=5)
        label2.place(x=200, y=5)
        label3.place(x=5, y=200)

        variants = ["Добавить студента", "Удалить студента", "Изменить данные студента"]
        self.__actions = Combobox(self.__main_window, values=variants)
        self.__actions.place(x=5, y=220)

        button = Button(text="Далее", command=self.change_data)
        button.place(x=5, y=250)
        self.make_groups_list()
        self.create_table_of_students()

        self.__main_window.mainloop()

    def change_table_of_students(self, event):
        students = []
        if len(self.__groups_list.curselection()) > 0:
            self.__students_table.delete(*self.__students_table.get_children())
            group_index = self.__groups_list.curselection()
            self.__chosen_group = self.__groups_list.get(group_index[0])
            with open(f"group{self.__chosen_group}.csv", "r", newline="") as file:
                reader = csv.reader(file)
                for student in reader:
                    students.append(student)

        for student in students:
            self.__students_table.insert("", END, values=student)

    def input_deleted_student(self):
        delete_student_window = Toplevel(self.__main_window)
        label1 = Label(delete_student_window, text="Введите ID Удаляемого студента")

        entry = Entry(delete_student_window)

        deleted_student_id = partial(self.delete_student, entry)
        button = Button(delete_student_window, text="Далее", command=deleted_student_id)

        button.place(x=5, y=65)
        label1.place(x=5, y=5)
        entry.place(x=5, y=25)

    def delete_student(self, deleted_student_id):
        deleted_data = deleted_student_id.get()
        group = Group(self.__chosen_group)
        group.delete_student(deleted_data)


    def change_student(self, name_entry, fname_entry, student_id_entry, email_entry):
        changed_student = None
        student_id = student_id_entry.get()
        with open(f"group{self.__chosen_group}.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for student in reader:
                if student[2] == student_id:
                    print(student[2])
                    changed_student = student

        if name_entry.get() != "":
            changed_student[0] = name_entry.get()
        elif fname_entry.get() != "":
            changed_student[1] = fname_entry.get()
        elif email_entry.get() != "":
            changed_student[3] = email_entry.get()

        group = Group(self.__chosen_group)
        group.change_student_Tk(changed_student)






    def input_new_student(self):
        input_student_window = Toplevel(self.__main_window)
        name = Label(input_student_window, text="Имя")
        fname = Label(input_student_window, text="Фамилия")
        student_id = Label(input_student_window, text="ID")
        email = Label(input_student_window, text="Email")

        name_entry = Entry(input_student_window)
        fname_entry = Entry(input_student_window)
        student_id_entry = Entry(input_student_window)
        email_entry = Entry(input_student_window)

        # new_student_name = name_entry.get()
        # new_student_fname = fname_entry.get()
        # new_student_id = student_id_entry.get()
        # new_student_email = email_entry.get()
        choice = self.__actions.get()
        if choice == "Добавить студента":
            make_action = partial(self.add_new_student, name_entry, fname_entry, student_id_entry, email_entry)
            button = Button(input_student_window, text="Добавить", command=make_action)
        else:
            make_action = partial(self.change_student, name_entry, fname_entry, student_id_entry, email_entry)
            button = Button(input_student_window, text="Добавить", command=make_action)

        name.place(x=5, y=5)
        name_entry.place(x=5, y=25)
        fname.place(x=5, y=45)
        fname_entry.place(x=5, y=65)
        student_id.place(x=5, y=85)
        student_id_entry.place(x=5, y=105)
        email.place(x=5, y=125)
        email_entry.place(x=5, y=145)
        button.place(x=5, y=170)





    def add_new_student(self, name_entry, fname_entry, student_id_entry, email_entry):
        new_student_data = [name_entry.get(), fname_entry.get(), student_id_entry.get(), email_entry.get()]
        group_data = Group(self.__chosen_group)
        group_data.add_new_students_tk(new_student_data)

        self.__main_window.update()

    def create_table_of_students(self):
        students_panel = PanedWindow(self.__main_window)
        students_panel.place(x=200, y=25)

        columns = ("name", "fname", "ID", "Email")
        self.__students_table = Treeview(students_panel, columns=columns, show="headings")
        self.__students_table.pack(fill=BOTH, expand=1)

        self.__students_table.heading("name", text="Имя")
        self.__students_table.heading("fname", text="Фамилия")
        self.__students_table.heading("ID", text="ID")
        self.__students_table.heading("Email", text="Email")

        self.__students_table.column("#1", stretch=NO, width=120)
        self.__students_table.column("#2", stretch=NO, width=120)
        self.__students_table.column("#3", stretch=NO, width=100)
        self.__students_table.column("#4", stretch=NO, width=200)

    def make_groups_list(self):
        groups_list_panel = PanedWindow(self.__main_window)
        groups_list_panel.place(x=5, y=30)
        all_groups = []

        with open(f"{self.__chosen_faculty}.csv", "r", newline="") as file:
            for group in file:
                all_groups.append(group[0])

        self.__groups_list = self.sort_groups(all_groups)
        groups_var = Variable(value=all_groups)
        self.__groups_list = Listbox(groups_list_panel, listvariable=groups_var)
        self.__groups_list.bind("<<ListboxSelect>>", self.change_table_of_students)
        self.__groups_list.pack(side=LEFT, fill=BOTH, expand=1)

        scrollbar = Scrollbar(groups_list_panel, orient="vertical", command=self.__groups_list.yview)
        scrollbar.pack(side=RIGHT, fill=Y)


        self.__groups_list["yscrollcommand"] = scrollbar.set



    def sort_groups(self, groups):
        for i in range(len(groups)):
            if i != len(groups) - 1:
                if groups[i] > groups[i + 1]:
                    groups[i], groups[i + 1] = groups[i + 1], groups[i]

        return groups





