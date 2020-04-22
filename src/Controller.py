from src.DiceSet import DiceSet


class Controller:
    def __init__(self):
        pass

    def run(self):
        try:
            data = self.__fetchInput()
            results = self.__getDiceResults(data)
            print(results)
        except Warning as warning:
            print(str(warning))

    def __fetchInput(self):
        print('Index schema: 1, 2, 3, 4, 5, 6')

        diceData = input("Please enter dice probabilities: ")
        diceData = self.__fixDiceData(diceData)
        self.__validateDiceData(diceData)
        diceData = diceData

        throwCount = input("Please enter a throw count: ")

        return [diceData, throwCount]

    def __fixDiceData(self, diceData):
        return str(diceData) \
            .replace(' ', '') \
            .replace('(', '') \
            .replace(')', '') \
            .split(',')

    def __validateDiceData(self, fixedInput):
        if len(fixedInput) == 6:
            return

        total = 0
        for number in fixedInput:
            total += int(number)

        if total == 100:
            return

        raise Warning('Invalid input')

    def __getDiceResults(self, data):
        return DiceSet().roll(data)
