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

    def setProbabilities(self, probabilities: List):
        self.__probabilities = probabilities

    def setDiceCount(self, diceCount: int):
        self.__diceCount = diceCount

    def setThrowCount(self, throwCount: int):
        self.__throwCount = throwCount

    def setAverage(self, average: float):
        self.__average = average

    def setDeviation(self, deviation: float):
        self.__deviation = deviation

    def print(self):
        thisFile: str = os.path.dirname(os.path.realpath(__file__))

        outFolder: str = thisFile + '/../out/'
        self.__createOutFolder(outFolder)

        logFile: str = outFolder + 'output.csv'
        isFile: bool = os.path.isfile(logFile)

        with open(logFile, 'a', newline='') as csvFile:
            if not isFile:
                self.__writeToNewFile(csvFile)
            else:
                self.__appendEntries(csvFile)

    def __createOutFolder(self, path: str):
        if not os.path.isdir(path):
            try:
                os.mkdir(path)
            except OSError:
                raise Warning("Creation of the output directory failed")

    def __writeToNewFile(self, csvFile: TextIO):
        fieldnames: List = ['entryDate', 'probabilities', 'diceCount', 'throwCount', 'average', 'deviation']
        writer: csv.DictWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({
            'entryDate': str(datetime.now()),
            'probabilities': str(self.__probabilities),
            'diceCount': self.__diceCount,
            'throwCount': self.__throwCount,
            'average': self.__average,
            'deviation': self.__deviation
        })

    def __appendEntries(self, csvFile: TextIO):
        writer: csv.writer = csv.writer(csvFile)
        writer.writerow([
            str(datetime.now()), str(self.__probabilities),
            self.__diceCount, self.__throwCount,
            self.__average, self.__deviation
        ])
