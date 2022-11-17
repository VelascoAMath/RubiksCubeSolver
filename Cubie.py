from dataclasses import dataclass
import numpy as np





@dataclass
class Cubie(object):

	pos:np.array = None


	def set_position(self, x, y, z):
		self.pos = np.array([[x], [y], [z]])

	def rotate(self, axis, angle):

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





def main():
	c = Cubie()

	c.set_position(1, 0, 0)
	c.rotate("z", 90)
	print(c)


if __name__ == '__main__':
	main()