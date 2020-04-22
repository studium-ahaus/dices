import random


class DiceSet:
    def roll(self, data):
        throwCount = data[1]
        diceData = data[0]
        results = []

        for i in range(throwCount):
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
