from dataclasses import dataclass
import numpy as np

from vpython import *


color_to_vec = {
	"r": vector(1, 0, 0),
	"w": vector(1, 1, 1),
	"b": vector(0, 0, 1),
	"g": vector(0, 1, 0),
	"o": vector(1, 0.5, 0),
	"y": vector(1, 1, 0),
}


def np_to_vector(x):
	'''
	Converts an np array in the form [[x], [y], [z]] into a vpython vector
	param: x - an np array
	returns: vpython vector
	'''
	return vector(x[2][0], x[1][0], x[0][0] )

@dataclass
class Cubie(object):
	'''
	This class represents an individual cubie that's found on a Rubik's cube
	'''

	# x,y,z position of the cubie
	pos         : np.array = None
	# Dictionary that maps each color to the norm of the surface on the face
	color_to_dir: dict     = None



	def set_position(self, x, y, z):
		'''
		Set the position of the cubie
		param x
		param y
		param z
		'''
		self.pos = np.array([[x], [y], [z]])
		self.color_to_dir = dict()

	def set_color(self, color, x, y, z):
		'''
		Adds a color with the norm of the face with that color
		param color - the color. Should be a string in 'rwbgoy'
		'''
		self.color_to_dir[color] = np.array([[x], [y], [z]])


	def rotate(self, axis, angle):

		'''
		param: axis - The axis of rotation
		param: angle - The amount (degrees) to rotate the cubie around the origin
		'''
		angle = np.radians(angle)

		if axis == 'x':
			R = np.array([[1, 0, 0], [0, np.cos( angle ), -np.sin(angle)], [0, np.sin(angle), np.cos(angle)]])
		elif axis == 'y':
			R = np.array([[np.cos( angle ),  0, np.sin(angle)], [0, 1, 0], [-np.sin(angle), 0, np.cos(angle)]])
		elif axis == 'z':
			R = np.array([[np.cos( angle ), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
		else:
			raise Exception(f"{axis} is not a valid axis! Must be x, y, or z!")

		self.pos = np.round(R @ self.pos)
		for color, v  in self.color_to_dir.items():
			self.color_to_dir[color] = np.round(R @ v)

	def render(self):
		'''
		Render the cubie using vpython
		'''
		for color, v in self.color_to_dir.items():
			# Face points forward/back
			if v[0][0] != 0:
				p1 = vertex(pos=np_to_vector(self.pos + v / 2 + np.array([[0], [0.5], [0.5]]) ), color=color_to_vec[color])
				p2 = vertex(pos=np_to_vector(self.pos + v / 2 + np.array([[0], [0.5], [-0.5]]) ), color=color_to_vec[color])
				p3 = vertex(pos=np_to_vector(self.pos + v / 2 + np.array([[0], [-0.5], [-0.5]]) ), color=color_to_vec[color])
				p4 = vertex(pos=np_to_vector(self.pos + v / 2 + np.array([[0], [-0.5], [0.5]]) ), color=color_to_vec[color])
			# Face points up/down
			elif v[1][0] != 0:
				p1 = vertex(pos=np_to_vector(self.pos + v / 2 + np.array([[0.5], [0], [0.5]]) ), color=color_to_vec[color])
				p2 = vertex(pos=np_to_vector(self.pos + v / 2 + np.array([[0.5], [0], [-0.5]]) ), color=color_to_vec[color])
				p3 = vertex(pos=np_to_vector(self.pos + v / 2 + np.array([[-0.5], [0], [-0.5]]) ), color=color_to_vec[color])
				p4 = vertex(pos=np_to_vector(self.pos + v / 2 + np.array([[-0.5], [0], [0.5]]) ), color=color_to_vec[color])
			# Face points left/right
			elif v[2][0] != 0:
				p1 = vertex(pos=np_to_vector(self.pos + v / 2 + np.array([[0.5], [0.5], [0]]) ), color=color_to_vec[color])
				p2 = vertex(pos=np_to_vector(self.pos + v / 2 + np.array([[0.5], [-0.5], [0]]) ), color=color_to_vec[color])
				p3 = vertex(pos=np_to_vector(self.pos + v / 2 + np.array([[-0.5], [-0.5], [0]]) ), color=color_to_vec[color])
				p4 = vertex(pos=np_to_vector(self.pos + v / 2 + np.array([[-0.5], [0.5], [0]]) ), color=color_to_vec[color])
			Q = quad(vs=[p1,p2,p3,p4])




def main():
	c1 = Cubie()
	c1.set_position(1, 1, 1)
	c1.set_color('r', 0, 1, 0)
	c1.set_color('w', 0, 0, 1)
	c1.set_color('b', 1, 0, 0)
	c1.rotate("z", 180)
	print(c1)
	c1.render()
	c2 = Cubie()
	c2.set_position(-1, -1, -1)
	c2.set_color('o', 0, -1, 0)
	c2.set_color('y', 0, 0, -1)
	c2.set_color('g', -1, 0, 0)
	c2.rotate("z", 180)
	print(c2)
	c2.render()


if __name__ == '__main__':
	main()
