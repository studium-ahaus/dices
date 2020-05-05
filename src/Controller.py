from typing import List

from src.DiceSet import DiceSet
from src.Plotter import Plotter


class Controller:
    def run(self):
        try:
            data: List = self.__fetchInput()
            diceResults: List = self.__getDiceResults(data)

            Plotter().plot(diceResults, data[2])
        except Warning as warning:
            print(str(warning))
        except KeyboardInterrupt:
            print('')

    def __fetchInput(self):
        print('Index schema: 1, 2, 3, 4, 5, 6')

        diceData: str = input("Please enter dice probabilities: ")
        diceData: List = self.__fixDiceData(diceData)
        self.__validateDiceData(diceData)

        diceCount: str = input("Please enter a dice count: ")
        diceCount: int = int(diceCount)

        throwCount: str = input("Please enter a throw count: ")
        throwCount: int = int(throwCount)

        return [diceData, diceCount, throwCount]

    def __fixDiceData(self, diceData: str):
        return str(diceData) \
            .replace(' ', '') \
            .replace('(', '') \
            .replace(')', '') \
            .split(',')

    def __validateDiceData(self, fixedInput: List):
        if len(fixedInput) != 6:
            raise Warning('Please enter all probabilities')

        total: float = 0
        for number in fixedInput:
            total += float(number)

        if total != 100:
            raise Warning('The sum of probabilities has to be 100')

    def __getDiceResults(self, data: List):
        return DiceSet().roll(data)
