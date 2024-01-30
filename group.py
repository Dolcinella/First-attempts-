import csv
import shutil
import pickle
from SuchStudentIDExistsException import SuchStudentIDExistsException
from backup import Backup
from student import Student
from group_UI import Group_UI


class Group:
    def __init__(self, group_number, faculty_name=0, step=0):
        self.__faculty_name = faculty_name
        self.__group_number = group_number
        self.__members = f"group{self.__group_number}.csv"
        self.__step = step
        self.__group_ui = Group_UI()

    def __str__(self):
        return f"Номер группы:{self.__group_number:10} Список студентов: {self.__members:10} Шаг{self.__step}"

    def get_group_number(self):
        return self.__group_number

    def get_group_members(self):
        return self.__members

    def get_step(self):
        return self.__step

    # def fill_group_personally(self):
    #     students = []
    #     choice = 1
    #     while choice == 1:
    #         new_student = Student_UI()
    #         new_student_data = new_student.input_student_UI()
    #         students.append([new_student_data.get_name(), new_student_data.get_family_name(),
    #                          new_student_data.get_student_id(), new_student_data.get_email()])
    #         choice = int(input("Продолжить - 1; \n Завершить - 2; \n Ваш выбор: "))

    # return students

    # def fill_new_group_personally(self):
    #     new_student = Student_UI()
    #     new_student_data = new_student.input_student_UI()
    #     with open(self.__members, "w", newline="") as file:
    #         writer = csv.writer(file)
    #         writer.writerows(new_student_data)

    def check_student_id(self, new_id):
        valid = False
        with open(self.__members, "r", newline="") as file:
            reader = csv.reader(file)
            for student in reader:
                if student[2] == new_id:
                    valid = True
                    break

        return valid

    def add_new_students(self):
        choice = 1
        self.create_backup()
        self.__step += 1
        while choice == 1:
            new_student_data = self.__group_ui.input_student_UI()
            if self.check_student_id(new_student_data[2]):
                raise SuchStudentIDExistsException
            with open(self.__members, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(new_student_data)
            choice = self.__group_ui.make_choice()

    def add_new_students_tk(self, new_student_data):
        self.create_backup()
        self.__step += 1
        with open(self.__members, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(new_student_data)

    def input_changed_student(self, new_student_data):
        with open(self.__members, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(new_student_data)

    def fill_group_by_file(self):
        file_name = self.__group_ui.input_file_name()
        shutil.copy2(file_name, self.__members)

    def find_student_by_ID(self, id):
        result = None

        with open(self.__members, "r", newline="") as file:
            reader = csv.reader(file)
            for student in reader:
                if student[2] == id:
                    result = [student[0], student[1], student[2], student[3]]
                    break

        return result

    def create_backup(self):
        backup = Backup(self.__members, f"group{self.__group_number}backup{self.__step + 1}.csv")
        backup.create_backup()
        # with open(f"group{self.__group_number}backup{self.__step + 1}.csv", "w", newline="") as file1:
        #     writer = csv.writer(file1)
        #     with open(self.__members, "r", newline="") as file2:
        #         reader = csv.reader(file2)
        #         for student in reader:
        #             writer.writerow(student)

    def delete_student(self, student_ID):
        self.create_backup()
        self.__step += 1
        with open(self.__members, "w", newline="") as file1:
            writer = csv.writer(file1)
            with open(f"group{self.__group_number}backup{self.__step}.csv", "r", newline="") as file2:
                reader = csv.reader(file2)
                for student in reader:
                    if student_ID != student[2]:
                        writer.writerow(student)

    def output_group_members(self):
        with open(self.__members, "r", newline="") as file:
            reader = csv.reader(file)
            for student in reader:
                result = Student(student[0], student[1], student[2], student[3])
                yield result  # Сделать проверку, является ли студентом

    def return_step(self):
        backup = Backup(self.__members, f"group{self.__group_number}backup{self.__step}.csv")
        self.__step -= 1
        backup.return_previous_step()

    # def add_student(self, student):
    #     new_student = [student.get_name(), student.get_family_name(), student.get_student_id(), student.get_email()]
    #     with open(self.__members, "a", newline="") as file:
    #         writer = csv.writer(file)
    #         writer.writerow(new_student)

    def change_student(self):
        student_ID = self.__group_ui.input_student_ID()
        choice = self.__group_ui.choose_parameter()
        new_name = self.__group_ui.input_new_name()
        changed_student = self.find_student_by_ID(student_ID)
        self.delete_student(student_ID)

        if choice == 1:
            changed_student[0] = new_name
        elif choice == 2:
            changed_student[1] = new_name
        else:
            changed_student[3] = new_name

        self.input_changed_student(changed_student)

    def change_student_Tk(self, changed_student):
        self.delete_student(changed_student[2])

        self.input_changed_student(changed_student)