# zu testzwecken noch vorhanden
import shutil

import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def plot(self, diceList):
        diceList = self.__convertList(diceList)
        totalThrows = sum(diceList)
        maxWidth = shutil.get_terminal_size().columns - 20

        if maxWidth <= 10:
            raise Warning("Terminal-window too small")

        print("Visual representation:")
        print("=" * 100)

        for j in range(1, 7):
            percentage = 100 * diceList[j - 1] / totalThrows
            bar = "#" * int(100 * diceList[j - 1] / totalThrows)

            print("] {} - {: >5}%: \t".format(j, percentage), bar)

        print("=" * 100)

    # Diagramm mit Matplotlib erstellen
    def plotAsDiagram(self, diceList, avg, dev, export=False):
        arrangedList = np.arange(0, len(diceList[0]) * 6, 0.001)
        gauss = self.__calculateGaussCurve(arrangedList, avg, dev)

        plt.xlabel("Eye-sum")
        plt.ylabel("Probability")
        plt.grid(True)

        colors = ['r', 'c', 'b', 'g']
        colors += list(reversed(colors))

        for j, color in zip(range(-4, 4), colors):
            plt.fill_between(arrangedList, gauss,
                             where=np.logical_and(arrangedList <= avg - (j * dev),
                                                  arrangedList >= avg - ((j + 1) * dev)), facecolor=color, alpha=0.5)

        plt.plot(range(1, len(diceList[0]) * 6 + 1),
                 [100 * j / len(diceList) for j in self.__convertListForDiagram(diceList)],
                 'ro', arrangedList, gauss)

        if export:
            plt.savefig("plot")

        plt.show()

    # Augenzahlen summieren und in einer Liste zurueckgeben
    def __convertListForDiagram(self, diceList):
        tmpList = []

        for j in diceList:
            tmpList.append(sum(j))

        outList = [0] * len(diceList[0]) * 6

        for j in tmpList:
            outList[j - 1] += 1

        return outList

    # Haeufigkeit von augenzahlen bestimmen und in einer Liste zurueckgeben
    def __convertList(self, diceList):
        numList = [0] * 6

        for j in range(7):
            numList[j - 1] = diceList.count(j)

        return numList

    # Gauss-Kurven-Werte an den Stellen in interator berechnen und zurueckgeben
    def __calculateGaussCurve(self, iterator, mu, sigma):
        result = [0] * len(iterator)

        for j in range(1, len(iterator) + 1):
            result[j - 1] = 100 * (
                    (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((iterator[j - 1] - mu) / sigma) ** 2 / 2))

        return result

# zu testzwecken noch vorhanden
# p = Plotter()

# lst = []
# throwCount = 100000
# for i in range(throwCount):
# tmp = []
# for _ in range(6):
# tmp.append(random.randint(1, 6))
# lst.append(tmp)

# print(lst)

# Mittelwert bestimmen
# average = sum([sum(item) for item in lst]) / len(lst)

# Standardabweichung bestimmen
# deviation = np.sqrt(sum([(sum(item) - average) ** 2 for item in lst]) / (throwCount - 1))

# als Diagramm mit matplotlib plotten
# p.plotAsDiagram(lst, average, deviation, True)
