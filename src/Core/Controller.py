from typing import List

from Core.DiceSet import DiceSet
from Core.Plotter import Plotter
from Core.Printer import Printer


class Controller:
    __printer: Printer

    def run(self):
        try:
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
        print('Index schema: 1, 2, 3, 4, 5, 6')

        diceData: str = input("Please enter dice probabilities: ")
        diceData: List = self.__fixDiceData(diceData)
        self.__validateDiceData(diceData)
        self.__printer.setProbabilities(diceData)

        diceCount: str = input("Please enter a dice count: ")
        diceCount: int = int(diceCount)
        self.__printer.setDiceCount(diceCount)

        throwCount: str = input("Please enter a throw count: ")
        throwCount: int = int(throwCount)
        self.__printer.setThrowCount(throwCount)

        return [diceData, diceCount, throwCount]

    def __fixDiceData(self, diceData: str) -> List:
        return str(diceData) \
            .replace(' ', '') \
            .replace('(', '') \
            .replace(')', '') \
            .split(',')

    def __validateDiceData(self, fixedInput: List):
        if len(fixedInput) != 6:
            raise Warning('Please enter exactly 6 probabilities')

        total: float = 0
        for number in fixedInput:
            total += float(number)

        if total != 100:
            raise Warning('The sum of probabilities has to be 100')

    def __getDiceResults(self, data: List) -> List:
        return DiceSet().roll(data)
