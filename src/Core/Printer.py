import csv
import os
from datetime import datetime
from typing import List, TextIO


class Printer:
    __probabilities: List
    __diceCount: int
    __throwCount: int
    __average: float
    __deviation: float

    def setProbabilities(self, probabilities: List) -> None:
        self.__probabilities = probabilities

    def setDiceCount(self, diceCount: int) -> None:
        self.__diceCount = diceCount

    def setThrowCount(self, throwCount: int) -> None:
        self.__throwCount = throwCount

    def setAverage(self, average: float) -> None:
        self.__average = average

    def setDeviation(self, deviation: float) -> None:
        self.__deviation = deviation

    def print(self) -> None:
        thisDir: str = os.path.dirname(os.path.realpath(__file__))

        if "build" in thisDir:
            outFolder: str = thisDir + '/../../../out/'
        else:
            outFolder: str = thisDir + '/../../out/'

        print(outFolder)

        self.__createOutFolder(outFolder)

        logFile: str = outFolder + 'output.csv'
        isFile: bool = os.path.isfile(logFile)

        with open(logFile, 'a', newline='') as csvFile:
            if not isFile:
                self.__writeToNewFile(csvFile)
            else:
                self.__appendEntries(csvFile)

        print('Saved statistics to: \033[95m\033[1m' + logFile + '\033[0m')

    def __createOutFolder(self, path: str) -> None:
        if not os.path.isdir(path):
            try:
                os.mkdir(path)
            except OSError:
                raise Warning("Creation of the output directory failed")

    def __writeToNewFile(self, csvFile: TextIO) -> None:
        fieldnames: List = ['entryDate', 'probabilities', 'diceCount', 'throwCount', 'average', 'deviation']
        writer: csv.DictWriter = csv.DictWriter(csvFile, fieldnames=fieldnames, delimiter=';')

        writer.writeheader()
        writer.writerow({
            'entryDate': str(datetime.now()),
            'probabilities': str(self.__probabilities),
            'diceCount': self.__numToString(self.__diceCount),
            'throwCount': self.__numToString(self.__throwCount),
            'average': self.__numToString(self.__average),
            'deviation': self.__numToString(self.__deviation)
        })

    def __numToString(self, num) -> str:
        return str(num).replace('.', ',')

    def __appendEntries(self, csvFile: TextIO) -> None:
        writer: csv.writer = csv.writer(csvFile)
        writer.writerow([
            str(datetime.now()),
            str(self.__probabilities),
            self.__numToString(self.__diceCount),
            self.__numToString(self.__throwCount),
            self.__numToString(self.__average),
            self.__numToString(self.__deviation)
        ])
