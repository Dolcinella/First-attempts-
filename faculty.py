import csv
import shutil

from GroupExistsException import GroupExistsException
from IncorrectChoiceException import IncorrectChoiceException
from IncorrectGroupNumberException import IncorrectGroupNumberException
from backup import Backup
from faculty_UI import Faculty_UI
from group import Group

GROUP = []


# with open("groupslist.csv", "r", newline="") as file2:
#     reader = csv.reader(file2)
#     for student in reader:
#             GROUP.append(student)

class Faculty:
    def __init__(self, name):
        self.__name = name
        self.__groups = f"{self.__name}.csv"
        self.__faculty_UI = Faculty_UI

    # def create_group_list(self):
    #     with open(self.__groups, "w", newline="") as file1:
    #         writer = csv.writer(file1)

    def check_group_existence(self, group_number):
        valid = False
        with open(self.__groups, "r", newline="") as file:
            reader = csv.reader(file)
            for group in reader:
                if group_number == group[0]:
                    valid = True
                    break

        return valid

    def find_group(self, group_number):
        with open(self.__groups, "r", newline="") as file:
            reader = csv.reader(file)
            for group in reader:
                if group[0] == group_number:
                    result = [group[0], group[1], group[2]]
                    break

        return result

    def create_group(self, new_group_number):
        if not self.check_group_existence(new_group_number):
            new_group = Group(new_group_number)
            with open(f"{self.__name}.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([new_group.get_group_number(), new_group.get_group_members(), new_group.get_step()])

            with open(f"group{new_group.get_group_number()}.csv", "w", newline="") as file:
                csv.writer(file)
        else:
            print("Такая группа существует")

    # def get_group_step(self, group_number):
    #     pass

    def open_group(self, group_number):
        with open(self.__groups, "r", newline="") as file:
            reader = csv.reader(file)
            for g in reader:
                if g[0] == str(group_number):
                    chosen_group = Group(g[0], 0, int(g[2]))

        return chosen_group

    def close_group(self, group):
        group_number = str(group.get_group_number())
        found_group = self.find_group(group_number)
        self.delete_group(group_number)
        found_group[2] = group.get_step()
        with open(self.__groups, "a", newline="") as file1:
            writer = csv.writer(file1)
            writer.writerow(found_group)


    def create_faculty(self):
        with open(f"{self.__name}.csv", "w", newline="") as file1:
            writer = csv.writer(file1)

    def create_faculty_changer(self):
        faculty_changer = Backup(self.__groups, "faculty-changer.csv")
        faculty_changer.create_backup()
        # with open("faculty-changer.csv", "w", newline="") as file1:
        #     writer = csv.writer(file1)
        #     with open(self.__groups, "r", newline="") as file2:
        #         reader = csv.reader(file2)
        #         for student in reader:
        #             writer.writerow(student)

    def delete_group(self, group_number):
        self.create_faculty_changer()
        with open(self.__groups, "w", newline="") as file1:
            writer = csv.writer(file1)
            with open("faculty-changer.csv", "r", newline="") as file2:
                reader = csv.reader(file2)
                for group in reader:
                    if group_number != group[0]:
                        writer.writerow(group)

    def output_groups(self):
        with open(self.__groups, "r", newline="") as file:
            reader = csv.reader(file)
            for group in reader:
                result = Group(group[0], group[1], group[2])
                yield result

