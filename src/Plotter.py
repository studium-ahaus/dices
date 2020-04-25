import os
import random

class Plotter:
	def plot(self, diceList):
		diceList = self.__convertList(diceList)
		totalThrows = sum(diceList)
		maxWidth = os.get_terminal_size().columns - 20

		if maxWidth <= 10:
			raise Warning("Terminal-window to small")

		for i in range(1, 7):
			print("{} - {:0>5}%: \t".format(i, 100*diceList[i-1]/totalThrows), "#"*int(100*diceList[i-1]/totalThrows))

	def __convertList(self, diceList):
		numList = [0]*6
		for i in range(7):
			numList[i-1] = diceList.count(i)
		return numList