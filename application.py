from faculty import Faculty
from student import Student


class Application:
    def process(self, faculty_name="philology"):
        choice = 1
        faculty = Faculty(faculty_name)
        while choice != 0:
            print("1 - Открыть группу")
            print("2 - Создать группу")
            print("3 - Вывести список групп")
            print("4 - Завершить")
            choice = int(input("Ваш выбор:"))
            if choice == 1:
                new_group = int(input("Введите номер группы"))
                group = faculty.open_group(new_group)
                group_choice = 1
                while group_choice != 0:
                    print("1 - Добавить нового студента")
                    print("2 - Поиск студента")
                    print("3 - Вывести список студентов")
                    print("4 - Удалить студента")
                    print("5 - Поменять информацию о студенте")
                    print("6 - Отменить действие")
                    print("0 - Завершить работу с группой")
                    group_choice = int(input("Что вы хотите сделать:"))

                    if group_choice == 1:
                        group.add_new_students()
                    elif group_choice == 2:
                        student_id = str(input("Введите студенческий id требуемого студента: "))
                        found_student = group.find_student_by_ID(student_id)
                        if found_student == None:
                            print("Такого студента нет")
                        else:
                            found_student = Student(found_student[0], found_student[1], found_student[2], found_student[3])
                            print(found_student)
                    elif group_choice == 3:
                        for s in group.output_group_members():
                            print(s)
                    elif group_choice == 4:
                        student_id = str(input("Введите студенческий id требуемого студента: "))
                        group.delete_student(student_id)
                    elif group_choice == 5:
                        group.change_student()
                    elif group_choice == 6:
                        group.return_step()
                    elif group_choice == 0:
                        faculty.close_group(group)

            elif choice == 2:
                new_group_number = int(input("Введите номер группы"))
                faculty.create_group(new_group_number)
            elif choice == 3:
                for g in faculty.output_groups():
                    print(g)
