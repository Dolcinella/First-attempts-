import csv
import shutil


class Backup:
    def __init__(self, main_file, backup_name):
        self.__main_file = main_file
        self.__backup_name = backup_name

    def create_backup(self):
        with open(self.__backup_name, "w", newline="") as file1:
            writer = csv.writer(file1)
            with open(self.__main_file, "r", newline="") as file2:
                reader = csv.reader(file2)
                for object in reader:
                    writer.writerow(object)


    def return_previous_step(self):
        with open("temp.csv", 'w+') as output, open(self.__main_file, 'r') as input:
            shutil.copyfileobj(input, output)
        with open(self.__main_file, 'w+') as output, open(self.__backup_name, 'r') as input:
            shutil.copyfileobj(input, output)
        with open(self.__backup_name, 'w+') as output, open("temp.csv", 'r') as input:
            shutil.copyfileobj(input, output)





