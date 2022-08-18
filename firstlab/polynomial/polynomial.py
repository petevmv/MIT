from collections import defaultdict

class Polynomial:

	# създаване на у-то
	# ако коефициента = 0 -> кореспондиращата позиция с него не участва в състава
	# степента на у-то зависи от броя на елементи в списъка минус 1 
	# (5 елемента -> у-е от 4та степен) 
	# 
	def __init__(self, coefficients):
		self.equation = ''
		self.coefficients = coefficients
		self.degree = len(coefficients) - 1

	def expresion_of_x(degree):
			equation = ''
			
			if degree == 0:
				equation = ''
			
			elif degree == 1:
				equation = 'z'
			
			else:
				equation = f'z**{degree}'
			
			return equation


	def val(self, value):
		result = [x * value ** (self.degree - idx)  for idx, x in enumerate(self.coefficients)]
		return sum(result)

	def __call__(self, x):
		return self.val(x)

	def add(self, other):
		p1 = self.coefficients
		p2 = other.coefficients
		if len(self.coefficients) < len(other.coefficients):
			p1 = [0] * (len(other.coefficients) - len(self.coefficients)) + p1
		if len(self.coefficients) > len(other.coefficients):
			p2 = [0] * (len(self.coefficients) - len(other.coefficients)) + p2
			# print(p2)
		element_wise = [x + y for x,y in zip(p1, p2)]
		return Polynomial(element_wise)

	
	def __add__(self, p):
		return self.add(p)

	def mul(self, other):
		if type(other) is int or type(other) is float:
			scalar = other
			equation_mul_by_scalar = [x * scalar for x in self.coefficients]
			return Polynomial(equation_mul_by_scalar)
		
		p1 = self.coefficients
		p2 = other.coefficients

		order_p1 = self.degree
		order_p2 = other.degree
		# print(p1,order_p1, p2, order_p2)
		
		tup_p1 = []
		tup_p2 = []
		
		for i in p1:
			tup_p1.append((i, order_p1))
			order_p1 -= 1
		for i in p2:
			tup_p2.append((i, order_p2))
			order_p2 -= 1
		tup_of_coeff_and_power = []
		for x in tup_p1:
			for y in tup_p2:
				tup_of_coeff_and_power.append((x[0] * y[0], x[1] + y[1]))
		# print(tup_of_coeff_and_power)

		# This block of code will add all coeffs of the same order
		d = defaultdict(float)

		for x, y in tup_of_coeff_and_power:
			d[y] += float(x)

		# returning to list structure to pass it to polynomial class
		result = []
		for x in d.items():
			result.append(x[1])

		return Polynomial(result)


	def __mul__(self, p):
		return self.mul(p)

	def __str__(self):
		equation = ''
		
		for idx, el in enumerate(self.coefficients):
			
			if el == 0:
				continue
			
			if el > 0:
				sing = '+'
			
			else: 
				sing = '-'
			
			equation = equation + f" {self.coefficients[idx]}{Polynomial.expresion_of_x(self.degree - idx)} {sing}"

		return equation.rstrip('+').strip()
	
	def __repr__(self):
		return str(tuple(self.coefficients))


# p1 = Polynomial([-1, 2, -3, 4])
# p2 = Polynomial([3, 4, 5])
# p3 = Polynomial([-10, 2, 1])
# p4 = Polynomial([1, 2, 0, 4])

p1 = Polynomial([1,2,3])
p2 = Polynomial([100, 200])


# print(p1.add(p2))
# print((p1 + p2)(10))
# print(p1(-1))
# print(p1.mul(2))
print(p1.mul(p2))
print(p1 * p2)
