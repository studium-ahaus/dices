from typing import List

from art import *

from src.DiceSet import DiceSet
from src.Plotter import Plotter
from src.Printer import Printer


# noinspection PyMethodMayBeStatic
class Controller:
    __printer: Printer

    def run(self) -> None:
        try:
            header = text2art("dices")
            print(header)

            self.__printer: Printer = Printer()

            data: List = self.__fetch_input()
            dice_results: List = self.__get_dice_results(data)

            Plotter(self.__printer).plot(dice_results, data[2])
            self.__printer.print()
        except Warning as warning:
            print(str(warning))
        except KeyboardInterrupt:
            print('')

    def __fetch_input(self) -> List:
        dice_data: List = self.__get_dice_data()
        dice_count: int = self.__get_dice_count()
        throw_count: int = self.__get_throw_count()

        return [dice_data, dice_count, throw_count]

    def __get_dice_data(self) -> List:
        dice_data: str = ''

        while not self.__is_valid_dice_data(dice_data):
            print('\033[92mPlease enter valid dice probabilities\033[0m')
            dice_data: str = input("=> \033[94m")
            print('\033[0m')

            dice_data: List = self.__fix_dice_data(dice_data)

        self.__printer.set_probabilities(dice_data)

        return dice_data

    def __fix_dice_data(self, dice_data: str) -> List:
        return str(dice_data) \
            .replace(' ', '') \
            .replace('(', '') \
            .replace(')', '') \
            .split(',')

    def __is_valid_dice_data(self, fixed_input: List) -> bool:
        if len(fixed_input) != 6:
            return False

        total: float = 0
        for number in fixed_input:
            total += float(number)

        if total != 100:
            return False

        return True

    def __get_dice_count(self) -> int:
        dice_count: int = self.__get_count('dice')
        self.__printer.set_dice_count(dice_count)

        return dice_count

    def __get_count(self, name: str) -> int:
        count: int = 0

        while not self.__is_valid_count(count):
            print('\033[92mPlease enter a valid ' + name + ' count' + '\033[0m')
            count: str = input("=> \033[94m")
            print('\033[0m')

            count: int = int(count)

        return count

    def __is_valid_count(self, count: int) -> bool:
        return count >= 1

    def __get_throw_count(self) -> int:
        throw_count: int = self.__get_count('throw')
        self.__printer.set_throw_count(throw_count)

        return throw_count

    def __get_dice_results(self, data: List) -> List:
        return DiceSet().roll(data)
