import random
from typing import List


# noinspection PyMethodMayBeStatic
class DiceSet:
    def roll(self, data: List) -> List:
        print('✨ Rolling dices')

        throw_count: int = data[2]
        dice_count: int = data[1]
        dice_data: List = data[0]

        results: List = []

        for _ in range(throw_count):
            results.append(
                self.__roll_dice(dice_count, dice_data))

        return results

    def __roll_dice(self, dice_count: int, dice_data: List) -> List:
        results: List = []

        for _ in range(dice_count):
            total: float = 0
            roll: float = random.random()
            possible_result: int = 1

            for chance in dice_data:
                chance: float = float(chance) / 100
                total += chance

                if roll < total:
                    results.append(possible_result)
                    break

                possible_result += 1

        return results
