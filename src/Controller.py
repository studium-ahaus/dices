from typing import List

from art import *

from src.DiceSet import DiceSet
from src.Plotter import Plotter
from src.Printer import Printer


class Controller:
    __printer: Printer

    def run(self) -> None:
        try:
            header = text2art("dices")
            print(header)

            self.__printer: Printer = Printer()

            data: List = self.__fetchInput()
            diceResults: List = self.__getDiceResults(data)

            Plotter(self.__printer).plot(diceResults, data[2])
            self.__printer.print()
        except Warning as warning:
            print(str(warning))
        except KeyboardInterrupt:
            print('')

    def __fetchInput(self) -> List:
        diceData: List = self.__getDiceData()
        diceCount: int = self.__getDiceCount()
        throwCount: int = self.__getThrowCount()

        return [diceData, diceCount, throwCount]

    def __getDiceData(self) -> List:
        diceData: str = ''

        while not self.__isValidDiceData(diceData):
            print('\033[92mPlease enter valid dice probabilities\033[0m')
            diceData: str = input("=> \033[94m")
            print('\033[0m')

            diceData: List = self.__fixDiceData(diceData)

        self.__printer.setProbabilities(diceData)

        return diceData

    def __fixDiceData(self, diceData: str) -> List:
        return str(diceData) \
            .replace(' ', '') \
            .replace('(', '') \
            .replace(')', '') \
            .split(',')

    def __isValidDiceData(self, fixedInput: List) -> bool:
        if len(fixedInput) != 6:
            return False

        total: float = 0
        for number in fixedInput:
            total += float(number)

        if total != 100:
            return False

        return True

    def __getDiceCount(self) -> int:
        diceCount: int = self.__getCount('dice')
        self.__printer.setDiceCount(diceCount)

        return diceCount

    def __getCount(self, name: str) -> int:
        count: int = 0

        while not self.__isValidCount(count):
            print('\033[92mPlease enter a valid ' + name + ' count' + '\033[0m')
            count: str = input("=> \033[94m")
            print('\033[0m')

            count: int = int(count)

        return count

    def __isValidCount(self, count: int) -> bool:
        return count >= 1

    def __getThrowCount(self) -> int:
        throwCount: int = self.__getCount('throw')
        self.__printer.setThrowCount(throwCount)

        return throwCount

    def __getDiceResults(self, data: List) -> List:
        return DiceSet().roll(data)
