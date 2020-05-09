from typing import List

import matplotlib.pyplot as plt
import numpy as np

from src import Printer


# noinspection PyMethodMayBeStatic
class Plotter:
    __printer: Printer

    def __init__(self, printer: Printer) -> None:
        self.__printer = printer

    def plot(self, dice_list: List, throw_count: int) -> None:
        print('✨ Calculating statistics')
        print('')

        average: float = self.__get_average(dice_list)
        print('Average: \033[95m\033[1m' + str(average) + '\033[0m')
        self.__printer.set_average(average)

        deviation: float = self.__get_standard_deviation(average, dice_list, throw_count)
        print('Standard deviation: \033[95m\033[1m' + str(deviation) + '\033[0m')
        print('')
        self.__printer.set_deviation(deviation)

        self.plot_as_diagram(dice_list, average, deviation)

    def __get_average(self, dice_list: List) -> float:
        if len(dice_list) == 0:
            raise Warning("No throw-results given. Dicelist shall not be empty.")
        return sum(
            [sum(item) for item in dice_list]
        ) / len(dice_list)

    def __get_standard_deviation(self, average: float, dice_list: List, throw_count: int) -> float:
        if throw_count == 1:
            return 0
        return np.sqrt(
            sum(
                [(sum(item) - average) ** 2 for item in dice_list])
            / (throw_count - 1)
        )

    def plot_as_diagram(self, dice_list: List, avg: float, dev: float) -> None:
        plt.xlabel("Eye-sum")
        plt.ylabel("Probability")
        plt.grid(True)

        lst: np.ndarray = np.arange(0, 1)
        gauss: List = [0]

        if dev != 0:
            lst: np.ndarray = np.arange(0, len(dice_list[0]) * 6, 0.001)
            gauss: List = self.__calculate_gauss_curve(lst, avg, dev)

            colors: List = ['r', 'c', 'b', 'g']
            colors += list(reversed(colors))

            for i, color in zip(range(-4, 4), colors):
                plt.fill_between(lst, gauss,
                                 where=np.logical_and(lst <= avg - (i * dev),
                                                      lst >= avg - ((i + 1) * dev)), facecolor=color, alpha=0.5)

        plt.plot(range(1, len(dice_list[0]) * 6 + 1),
                 [100 * i / len(dice_list) for i in self.__convert_list_for_diagram(dice_list)],
                 'ro', lst, gauss)

        plt.show()

    def __calculate_gauss_curve(self, iterator: np.ndarray, mu: float, sigma: float) -> List:
        lst: List = [0] * len(iterator)

        for i in range(1, len(iterator) + 1):
            lst[i - 1] = 100 * (
                    (1 / (sigma * np.sqrt(2 * np.pi))) *
                    np.exp(-((iterator[i - 1] - mu) / sigma) ** 2 / 2)
            )

        return lst

    def __convert_list_for_diagram(self, dice_list: List) -> List:
        tmp_list: List = []

        for i in dice_list:
            tmp_list.append(sum(i))

        out_list: List = [0] * len(dice_list[0]) * 6

        for i in tmp_list:
            out_list[i - 1] += 1

        return out_list
