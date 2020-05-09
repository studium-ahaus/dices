import csv
import os
from datetime import datetime
from typing import List, TextIO


# noinspection PyMethodMayBeStatic
class Printer:
    __probabilities: List
    __dice_count: int
    __throw_count: int
    __average: float
    __deviation: float

    def set_probabilities(self, probabilities: List) -> None:
        self.__probabilities = probabilities

    def set_dice_count(self, dice_count: int) -> None:
        self.__dice_count = dice_count

    def set_throw_count(self, throw_count: int) -> None:
        self.__throw_count = throw_count

    def set_average(self, average: float) -> None:
        self.__average = average

    def set_deviation(self, deviation: float) -> None:
        self.__deviation = deviation

    def print(self) -> None:
        this_dir: str = os.path.dirname(os.path.realpath(__file__))
        out_folder: str = this_dir + '/../out/'

        self.__create_out_folder(out_folder)

        log_file: str = out_folder + 'output.csv'
        is_file: bool = os.path.isfile(log_file)

        with open(log_file, 'a', newline='') as csvFile:
            if not is_file:
                self.__write_to_new_file(csvFile)
            else:
                self.__append_entries(csvFile)

        print('Saved statistics to: \033[95m\033[1m' + log_file + '\033[0m')

    def __create_out_folder(self, path: str) -> None:
        if not os.path.isdir(path):
            try:
                os.mkdir(path)
            except OSError:
                raise Warning("\033[1m\033[91mCreation of the output directory failed\033[0m")

    def __write_to_new_file(self, csv_file: TextIO) -> None:
        fieldnames: List = ['entryDate', 'probabilities', 'diceCount', 'throwCount', 'average', 'deviation']
        writer: csv.DictWriter = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')

        writer.writeheader()
        writer.writerow({
            'entryDate': str(datetime.now()),
            'probabilities': str(self.__probabilities),
            'diceCount': self.__num_to_string(self.__dice_count),
            'throwCount': self.__num_to_string(self.__throw_count),
            'average': self.__num_to_string(self.__average),
            'deviation': self.__num_to_string(self.__deviation)
        })

    def __num_to_string(self, num) -> str:
        return str(num).replace('.', ',')

    def __append_entries(self, csv_file: TextIO) -> None:
        writer: csv.writer = csv.writer(csv_file)
        writer.writerow([
            str(datetime.now()),
            str(self.__probabilities),
            self.__num_to_string(self.__dice_count),
            self.__num_to_string(self.__throw_count),
            self.__num_to_string(self.__average),
            self.__num_to_string(self.__deviation)
        ])
