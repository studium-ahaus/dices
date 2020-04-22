import math
import random

class Result:
	standardDeviation = 0
	average = 0

	def __init__(self, deviation, avg):
		self.standardDeviation = deviation
		self.average = avg
		
	def getStandardDeviation(self):
		return self.standardDeviation

	def getAverage(self):
		return self.average

class Sample:
	lst = []
	count = 0

	def __init__(self):
		self.count = 1000000
		for i in range(self.count):
			self.lst.append(random.randint(1, 6))
	
	def throwCount(self):
		return self.count
	
	def throwResult(self):
		return self.lst

class Calculator:
	res = None

	def __init__(self, resObject):
		count = resObject.throwCount()
		lst = resObject.throwResult()

		average = self.__getAverage(lst, count)
		deviation = self.__getStandardDeviation(lst, count, average)
		self.res = Result(deviation, average)

	def __calculateDifferences(self, lst, average):
		total = 0
		for i in lst:
			total += (i - average)**2 

		return total

	def __getStandardDeviation(self, lst, count, average):
		return math.sqrt(
			self.__calculateDifferences(lst, average) / (count - 1)
		)

	def __getAverage(self, lst, count):
		return sum(lst)/count
	
	def getResult(self):
		return self.res