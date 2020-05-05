from typing import List

import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def plot(self, diceList: List, throwCount: int):
        average: float = self.__getAverage(diceList)
        print('Average: ' + str(average))

        deviation: float = self.__getStandardDeviation(average, diceList, throwCount)
        print('Standard deviation: ' + str(deviation))

        self.plotAsDiagram(diceList, average, deviation)

    def __getAverage(self, diceList: List):
        return sum(
            [sum(item) for item in diceList]
        ) / len(diceList)

    def __getStandardDeviation(self, average: float, diceList: List, throwCount: int):
        return np.sqrt(
            sum(
                [(sum(item) - average) ** 2 for item in diceList])
            / (throwCount - 1)
        )

    def plotAsDiagram(self, diceList: List, avg: float, dev: float):
        lst: np.ndarray = np.arange(0, len(diceList[0]) * 6, 0.001)
        gauss: List = self.__calculateGaussCurve(lst, avg, dev)

        plt.xlabel("Eye-sum")
        plt.ylabel("Probability")
        plt.grid(True)

        colors: List = ['r', 'c', 'b', 'g']
        colors += list(reversed(colors))

        for i, color in zip(range(-4, 4), colors):
            plt.fill_between(lst, gauss,
                             where=np.logical_and(lst <= avg - (i * dev),
                                                  lst >= avg - ((i + 1) * dev)), facecolor=color, alpha=0.5)

        plt.plot(range(1, len(diceList[0]) * 6 + 1),
                 [100 * i / len(diceList) for i in self.__convertListForDiagram(diceList)],
                 'ro', lst, gauss)

        plt.savefig("plot")
        plt.show()

    def __calculateGaussCurve(self, iterator: np.ndarray, mu: float, sigma: float):
        lst: List = [0] * len(iterator)

        for i in range(1, len(iterator) + 1):
            lst[i - 1] = 100 * (
                    (1 / (sigma * np.sqrt(2 * np.pi))) *
                    np.exp(-((iterator[i - 1] - mu) / sigma) ** 2 / 2)
            )

        return lst

    def __convertListForDiagram(self, diceList: List):
        tmpList: List = []

        for i in diceList:
            tmpList.append(sum(i))

        outList: List = [0] * len(diceList[0]) * 6

        for i in tmpList:
            outList[i - 1] += 1

        return outList
