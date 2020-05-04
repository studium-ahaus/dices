import shutil
import matplotlib.pyplot as plt
import numpy as np

# zu testzwecken noch vorhanden
import random


class Plotter:
    def __init__(self):
        pass

    # Diagramm in der Konsole erstellen
    def plot(self, diceList):
        diceList = self.__convertList(diceList)
        totalThrows = sum(diceList)
        maxWidth = shutil.get_terminal_size().columns - 20

        if maxWidth <= 10:
            raise Warning("Terminal-window too small")

        print("Visual representation:")
        print("=" * 100)

        for i in range(1, 7):
            percentage = 100 * diceList[i - 1] / totalThrows
            bar = "#" * int(100 * diceList[i - 1] / totalThrows)

            print("] {} - {: >5}%: \t".format(i, percentage), bar)

        print("=" * 100)

    # Diagramm mit Matplotlib erstellen
    def plotAsDiagram(self, dicelist, average, deviation, export=False):
        lst = np.arange(0, len(dicelist[0])*6, 0.001)
        gauss = self.__calculateGaussCurve(lst, average, deviation)
        
        plt.xlabel("Eye-sum")
        plt.ylabel("Probability")
        plt.grid(True)
        colors = ['r', 'c', 'b', 'g']
        colors += list(reversed(colors))

        for i, color in zip(range(-4, 4), colors):
            plt.fill_between(lst , gauss, 
             where=np.logical_and(lst <= average - (i * deviation), 
             lst >= average - ((i + 1) * deviation)), facecolor=color, alpha=0.5)

        plt.plot(range(1, len(dicelist[0]) * 6 + 1),
         [100*i/len(dicelist) for i in self.__convertListForDiagram(dicelist)],
         'ro', lst, gauss)

        if export:
            plt.savefig("plot")

        plt.show()

    # Augenzahlen summieren und in einer Liste zurueckgeben
    def __convertListForDiagram(self, diceList):
        tmpList = []
        for i in diceList:
            tmpList.append(sum(i))
        outList = [0]*len(diceList[0])*6
        
        for i in tmpList:
            outList[i - 1] += 1
        
        return outList

    # Haeufigkeit von augenzahlen bestimmen und in einer Liste zurueckgeben
    def __convertList(self, diceList):
        numList = [0] * 6
        for i in range(7):
            numList[i - 1] = diceList.count(i)

        return numList

    # Gauss-Kurven-Werte an den Stellen in interator berechnen und zurueckgeben
    def __calculateGaussCurve(self, iterator, mu, sigma):
        lst = [0]* len(iterator)
        for i in range(1, len(iterator) + 1):
            lst[i-1] = 100 * ( (1/(sigma * np.sqrt(2 * np.pi)))*np.exp(-((iterator[i-1]-mu)/sigma)**2/2) )
        return lst


# zu testzwecken noch vorhanden
p = Plotter()

lst = []
throwCount = 100000
for i in range(throwCount):
    tmp = []
    for _ in range(6):
        tmp.append(random.randint(1,6))
    lst.append(tmp)

# Mittelwert bestimmen
average = sum([sum(item) for item in lst])/len(lst)

# Standardabweichung bestimmen
deviation = np.sqrt(sum([(sum(item)-average)**2 for item in lst])/(throwCount-1))

# als Diagramm mit matplotlib plotten
p.plotAsDiagram(lst, average, deviation, True)