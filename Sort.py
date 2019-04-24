#Created by Guru Sarath
#25 April 2019

import matplotlib.pyplot as plt
import random as rnd

X = []
aryY = []

for i in range(20):
	X.extend([i+1])
	aryY.extend([i])


rnd.shuffle(aryY)

plt.figure(1)
plt.ion()
plt.bar(X, aryY, label = 'Sorting')
plt.show()
plt.pause(2)

def bubbleSort():

	for i in range(len(aryY) - 1):

		for j in range(len(aryY) - i - 1):

			if aryY[j] > aryY[j+1]:
				temp = aryY[j]
				aryY[j] = aryY[j+1]
				aryY[j+1] = temp

			plt.clf()
			plt.bar(X, aryY, label = 'Bubble Sorting')
			plt.pause(0.0001)

	return None

def insertionSort():

	for i in range(len(aryY) - 1):

		j = i

		while (aryY[j+1] < aryY[j] and j >= 0):
			temp = aryY[j+1]
			aryY[j+1] = aryY[j]
			aryY[j] = temp
			j = j - 1

			plt.clf()
			plt.bar(X, aryY, label = 'Insertion Sorting')
			plt.pause(0.0001)

	return None


rnd.shuffle(aryY)
bubbleSort()
plt.pause(3)

rnd.shuffle(aryY)
insertionSort()
plt.pause(3)