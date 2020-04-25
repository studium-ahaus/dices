import shutil


class Plotter:
    def plot(self, diceList):
        diceList = self.__convertList(diceList)
        totalThrows = sum(diceList)
        maxWidth = shutil.get_terminal_size().columns - 20

        if maxWidth <= 10:
            raise Warning("Terminal-window to small")

        print("Visual representation:")
        print("=" * 100)

        for i in range(1, 7):
            percentage = 100 * diceList[i - 1] / totalThrows
            bar = "#" * int(100 * diceList[i - 1] / totalThrows)

            print("] {} - {: >5}%: \t".format(i, percentage), bar)

        print("=" * 100)

    def __convertList(self, diceList):
        numList = [0] * 6
        for i in range(7):
            numList[i - 1] = diceList.count(i)

        return numList
