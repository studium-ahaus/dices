import random
from typing import List


class DiceSet:
    def roll(self, data: List) -> List:
        print('✨ Rolling dices')

        throwCount: int = data[2]
        diceCount: int = data[1]
        diceData: List = data[0]

        results: List = []

        for _ in range(throwCount):
            results.append(
                self.__rollDice(diceCount, diceData))

        return results

    def __rollDice(self, diceCount: int, diceData: List) -> List:
        results: List = []

        for _ in range(diceCount):
            total: float = 0
            roll: float = random.random()
            possibleResult: int = 1

            for chance in diceData:
                chance: float = float(chance) / 100
                total += chance

                if roll < total:
                    results.append(possibleResult)
                    break

                possibleResult += 1

        return results
