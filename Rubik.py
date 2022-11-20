from Cubie import Cubie
from dataclasses import dataclass
import numpy as np


@dataclass
class Rubik(object):
	'''
	This class represents a 3x3x3 Rubik's cube
	'''

	# list of cubies
	cubie_list : list = None

	def __init__(self, file_n):

		self.cubie_list = []

		# Reading in the input
		# Should be in this format
		# www
		# www
		# www
		# rrrbbboooggg
		# rrrbbboooggg
		# rrrbbboooggg
		# yyy
		# yyy
		# yyy
		read_string = []
		with open(file_n, 'r') as f:
			for l in f:
				l = l.rstrip()
				read_string.append(l)
		n = len(read_string) // 3

		# Create the cubies
		pos_to_cubie = {}
		for i in range(-1, 2):
			for j in range(-1, 2):
				for k in range(-1, 2):
					if i != 0 or j != 0 or k != 0:
						c = Cubie()
						c.set_position(i, j, k)
						pos_to_cubie[(i, j, k)] = c

		# Get the colors for every face
		U = read_string[3:6]

		pos_to_cubie[(-1, 1, 1)].set_color(U[0][0], 0, 1, 0)
		pos_to_cubie[(0, 1, 1)].set_color(U[0][1], 0, 1, 0)
		pos_to_cubie[(1, 1, 1)].set_color(U[0][2], 0, 1, 0)

		pos_to_cubie[(-1, 1, 0)].set_color(U[1][0], 0, 1, 0)
		pos_to_cubie[(0, 1, 0)].set_color(U[1][1], 0, 1, 0)
		pos_to_cubie[(1, 1, 0)].set_color(U[1][2], 0, 1, 0)
		
		pos_to_cubie[(-1, 1, -1)].set_color(U[2][0], 0, 1, 0)
		pos_to_cubie[(0, 1, -1)].set_color(U[2][1], 0, 1, 0)
		pos_to_cubie[(1, 1, -1)].set_color(U[2][2], 0, 1, 0)

		F = [x[3:6] for x in read_string[3:6]]

		pos_to_cubie[(1, 1, 1)].set_color(F[0][0], 1, 0, 0)
		pos_to_cubie[(1, 0, 1)].set_color(F[0][1], 1, 0, 0)
		pos_to_cubie[(1, -1, 1)].set_color(F[0][2], 1, 0, 0)

		pos_to_cubie[(1, 1, 0)].set_color(F[1][0], 1, 0, 0)
		pos_to_cubie[(1, 0, 0)].set_color(F[1][1], 1, 0, 0)
		pos_to_cubie[(1, -1, 0)].set_color(F[1][2], 1, 0, 0)
		
		pos_to_cubie[(1, 1, -1)].set_color(F[2][0], 1, 0, 0)
		pos_to_cubie[(1, 0, -1)].set_color(F[2][1], 1, 0, 0)
		pos_to_cubie[(1, -1, -1)].set_color(F[2][2], 1, 0, 0)

		D = [x[6:9] for x in read_string[3:6]]

		pos_to_cubie[(1, -1, 1)].set_color(D[0][0], 0, -1, 0)
		pos_to_cubie[(0, -1, 1)].set_color(D[0][1], 0, -1, 0)
		pos_to_cubie[(-1, -1, 1)].set_color(D[0][2], 0, -1, 0)

		pos_to_cubie[(1, -1, 0)].set_color(D[1][0], 0, -1, 0)
		pos_to_cubie[(0, -1, 0)].set_color(D[1][1], 0, -1, 0)
		pos_to_cubie[(-1, -1, 0)].set_color(D[1][2], 0, -1, 0)
		
		pos_to_cubie[(1, -1, -1)].set_color(D[2][0], 0, -1, 0)
		pos_to_cubie[(0, -1, -1)].set_color(D[2][1], 0, -1, 0)
		pos_to_cubie[(-1, -1, -1)].set_color(D[2][2], 0, -1, 0)


		B = [x[9:12] for x in read_string[3:6]]

		pos_to_cubie[(-1, -1, 1)].set_color(B[0][0], -1, 0, 0)
		pos_to_cubie[(-1, 0, 1)].set_color(B[0][1], -1, 0, 0)
		pos_to_cubie[(-1, 1, 1)].set_color(B[0][2], -1, 0, 0)

		pos_to_cubie[(-1, -1, 0)].set_color(B[1][0], -1, 0, 0)
		pos_to_cubie[(-1, 0, 0)].set_color(B[1][1], -1, 0, 0)
		pos_to_cubie[(-1, 1, 0)].set_color(B[1][2], -1, 0, 0)
		
		pos_to_cubie[(-1, -1, -1)].set_color(B[2][0], -1, 0, 0)
		pos_to_cubie[(-1, 0, -1)].set_color(B[2][1], -1, 0, 0)
		pos_to_cubie[(-1, 1, -1)].set_color(B[2][2], -1, 0, 0)

		L = read_string[6:9]
		pos_to_cubie[(-1, 1, -1)].set_color(L[0][0], 0, 0, -1)
		pos_to_cubie[(0, 1, -1)].set_color(L[0][1], 0, 0, -1)
		pos_to_cubie[(1, 1, -1)].set_color(L[0][2], 0, 0, -1)

		pos_to_cubie[(-1, 0, -1)].set_color(L[1][0], 0, 0, -1)
		pos_to_cubie[(0, 0, -1)].set_color(L[1][1], 0, 0, -1)
		pos_to_cubie[(1, 0, -1)].set_color(L[1][2], 0, 0, -1)
		
		pos_to_cubie[(-1, -1, -1)].set_color(L[2][0], 0, 0, -1)
		pos_to_cubie[(0, -1, -1)].set_color(L[2][1], 0, 0, -1)
		pos_to_cubie[(1, -1, -1)].set_color(L[2][2], 0, 0, -1)


		R = read_string[0:3]
		pos_to_cubie[(-1, -1, 1)].set_color(R[0][0], 0, 0, 1)
		pos_to_cubie[(0, -1, 1)].set_color(R[0][1], 0, 0, 1)
		pos_to_cubie[(1, -1, 1)].set_color(R[0][2], 0, 0, 1)

		pos_to_cubie[(-1, 0, 1)].set_color(R[1][0], 0, 0, 1)
		pos_to_cubie[(0, 0, 1)].set_color(R[1][1], 0, 0, 1)
		pos_to_cubie[(1, 0, 1)].set_color(R[1][2], 0, 0, 1)
		
		pos_to_cubie[(-1, 1, 1)].set_color(R[2][0], 0, 0, 1)
		pos_to_cubie[(0, 1, 1)].set_color(R[2][1], 0, 0, 1)
		pos_to_cubie[(1, 1, 1)].set_color(R[2][2], 0, 0, 1)


		# Only store the cubies with colors (AKA the visible ones)
		for pos in pos_to_cubie:
			if len(pos_to_cubie[pos].color_to_dir) == 0:
				continue
			self.cubie_list.append(pos_to_cubie[pos])

		self.cubie_list.sort()



	def rotate(self, move_list):
		'''
		Rotates the rubik's cube.
		Valid moves are U, F, B, D, L, and F.
		We also allow ' versions (e.g. U', F', etc) and 2 version (U2, F2, etc)
		param: move - The move you wish to perform
		'''

		if isinstance(move_list, str):
			move_list = [move_list]

		for move in move_list:
			if move[0] not in {"U", "D", "R", "L", "F", "B"}:
				raise Exception(f"Unrecognized {move=}!")

			for cube in self.cubie_list:
				axis = None
				angle = None
				if move[0] == "U" and cube.get_y() == 1:
					axis = "y"
					angle = 90
				elif move[0] == "D" and cube.get_y() == -1:
					axis = "y"
					angle = -90
				elif move[0] == "R" and cube.get_z() == 1:
					axis = "z"
					angle = 90
				elif move[0] == "L" and cube.get_z() == -1:
					axis = "z"
					angle = -90
				elif move[0] == "F" and cube.get_x() == 1:
					axis = "x"
					angle = 90
				elif move[0] == "B" and cube.get_x() == -1:
					axis = "x"
					angle = -90

				if axis is None or angle is None:
					continue
				if len(move) == 2 and move[1]=="'":
					angle *= -1
				
				if len(move) == 2 and move[1]=="2":
					angle *= 2

				cube.rotate(axis, angle)
		self.cubie_list.sort()

	def __hash__(self):
		result_hash = 0
		for cubie in self.cubie_list:
			result_hash ^= hash(cubie)

		return result_hash

	def render(self):
		'''
		Render the cube using vpython
		'''
		for cube in self.cubie_list:
			cube.render()



def main():
	c = Rubik('test1')

	c.rotate(["R'", "D'", "R", "D"])
	print(c)
	c.render()


if __name__ == '__main__':
	main()
