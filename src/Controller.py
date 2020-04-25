from src.Calculator import Calculator
from src.DiceSet import DiceSet
from src.Plotter import Plotter


class Controller:
    def run(self):
        try:
            data = self.__fetchInput()
            diceResults = self.__getDiceResults(data)
            calResults = Calculator(diceResults).getResult()

            print('Standard deviation: ' + str(calResults.getStandardDeviation()))
            print('Average: ' + str(calResults.getAverage()))
            Plotter().plot(diceResults)
        except Warning as warning:
            print(str(warning))
        except KeyboardInterrupt:
            print('')

    def __fetchInput(self):
        print('Index schema: 1, 2, 3, 4, 5, 6')

        diceData = input("Please enter dice probabilities: ")
        diceData = self.__fixDiceData(diceData)
        self.__validateDiceData(diceData)

        throwCount = input("Please enter a throw count: ")
        throwCount = int(throwCount)

        return [diceData, throwCount]

    def __fixDiceData(self, diceData):
        return str(diceData) \
            .replace(' ', '') \
            .replace('(', '') \
            .replace(')', '') \
            .split(',')

    def __validateDiceData(self, fixedInput):
        if len(fixedInput) != 6:
            raise Warning('Please enter all probabilities')

        total = 0
        for number in fixedInput:
            total += float(number)

        if total != 100:
            raise Warning('The sum of probabilities has to be 100')

    def __getDiceResults(self, data):
        return DiceSet().roll(data)
