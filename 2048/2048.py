"""
2048 GAME Implementation
"""
import numpy as np
import random
import itertools
from arrow_keys import get_key


class Game:
	# Default constructor
	def __init__(self, dim=4, target=2048, display=True):
		self.matrix = np.array([[0 for _ in range(dim)] for _ in range(dim)])
		self.dim = dim
		self.target = target
		self.score = 0
		self.display = display
		self.__DIRECTION_MAPPER = {
			"left" : self.matrix,
			"right" : self.matrix.T[::-1].T,
			"up" : self.matrix.T,
			"down" : self.matrix[::-1].T,
			}
		self.place_random(True)
		self.place_random(True)
		if self.display:
			print(self.__str__())
		self.old_state = np.array([])

	# Shifts - up, down, left, right
	def shift(self, direction):
		flag = False
		for row in self.__DIRECTION_MAPPER[direction]:
			i = 0
			j = i + 1
			while(i<j):
				if row[j] == 0:
					j += 1
				elif row[i] == 0:
					row[i] = row[j]
					row[j] = 0
					j += 1
					flag = True
				elif row[i] == row[j]:
					row[i] += row[j]
					self.score += row[i]
					row[j] = 0
					j += 1
					i += 1
					flag = True
				elif row[i] != row[j]:
					i += 1
					j = i + 1
				if j == self.dim:
					break

		if self.display:
			print("Score : {}".format(self.score))
		if self.max_found():
			self.end_condition(True)
		self.place_random(flag)
		if self.display:
			print(self.__str__())
		if np.array_equal(self.old_state, self.matrix):
			return False
		self.old_state = self.matrix.copy()
		return True

	# insert 2 or 4 randomly on voids and check for end game
	def place_random(self, flag=False):
		cell = self.get_empty_cell()
		if cell:
			if flag:
				x,y = cell
				self.matrix[x][y] = random.choice([2, 2, 2, 2, 2, 4, 2, 2, 2, 2])

		cell = self.get_empty_cell()		
		if not cell and not self.scope():
			self.end_condition(False)
	
	# scope of move
	def scope(self):
		for i in range(0, self.dim):
			for j in range(0, self.dim):
				if j+1 < self.dim and self.matrix[i][j] == self.matrix[i][j+1]:
					return True
				if i+1 < self.dim and self.matrix[i][j] == self.matrix[i+1][j]:
					return True
		return False

	# check for voids
	def get_empty_cell(self):
		empty = [(i,j) for i,j in itertools.product(range(self.dim),range(self.dim)) if self.matrix[i][j]==0]
		if len(empty) == 0:
			return False
		return empty[random.randint(0,len(empty)-1)]

	# check if target is reached
	def max_found(self):
		max_sum = np.max(self.matrix)
		if max_sum == self.target:
			return True
		return False

	# default print
	def __str__(self):
		return self.matrix

	# end game
	def end_condition(self, flag):
		if not self.display:
			return
		if flag:
			print("You Win")
		else:
			print("You Lose")
		if self.display:
			print(self.__str__())
		exit()


if __name__ == '__main__':
	game = Game(dim=4, target=2048, display=True)
	while True:
		k = get_key()
		game.shift(k)
