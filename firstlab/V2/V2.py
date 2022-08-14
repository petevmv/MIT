class V2:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return f'({self.x}, {self.y})'

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def __add__(self, other):
		x_new_v = self.x + other.x
		y_new_v = self.y + other.y
		return V2(x_new_v, y_new_v)

	def add(self, other):
		x_new_v = self.x + other.x
		y_new_v = self.y + other.y
		return V2(x_new_v, y_new_v)

	def __mul__(self, other):
		x_new_with_scalar = self.x * scalar
		y_new_with_scalar = self.y * scalar
		return(V2(x_new_with_scalar, y_new_with_scalar))

	def mul(self, scalar):
		x_new_with_scalar = self.x * scalar
		y_new_with_scalar = self.y * scalar
		return(V2(x_new_with_scalar, y_new_with_scalar))

	def __mul__(self, v):
		return self.mul(v)
			


v1 = V2(1, 2)
# print(v1.getX())
# print(v1.getY())
v2 = V2(3, 4)

print(v1 + v2)
print(v1.mul(2))

# print(v1.add(v2).mul(-1))

