import random


class DiceSet:
    def roll(self, data):
        throwCount = data[2]
        diceCount = data[1]
        diceData = data[0]

        results = []

        for _ in range(throwCount):
            results.append(
                self.__rollDice(diceCount, diceData))

        return results

    def __rollDice(self, diceCount, diceData):
        results = []

        for _ in range(diceCount):
            total = 0
            roll = random.random()
            possibleResult = 1

            for chance in diceData:
                chance = float(chance) / 100
                total += chance

                if roll < total:
                    results.append(possibleResult)
                    break

                possibleResult += 1

        return results
