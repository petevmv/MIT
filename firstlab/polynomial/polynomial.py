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


	def expr_x(degree):
			equation = ''
			
			if degree == 0:
				equation = ''
			
			elif degree == 1:
				equation = 'z'
			
			else:
				equation = f'z**{degree}'
			
			return equation


	def __str__(self):
		equation = ''
		
		for idx, el in enumerate(self.coefficients):
			
			if el == 0:
				continue
			
			if el > 0:
				sing = '+'
			
			else: 
				sing = '-'
			
			equation = equation + f" {self.coefficients[idx]}{Polynomial.expr_x(self.degree - idx)} {sing}"

		return equation.rstrip('+').strip()
	
	def __repr__(self):
		return str(tuple(self.coefficients))


# p1 = Polynomial([-1, 2, -3, 4])
# p2 = Polynomial([3, 4, 5])
# p3 = Polynomial([-10, 2, 1])
# p4 = Polynomial([1, 2, 0, 4])

p1 = Polynomial([1,2,3])
# p2 = Polynomial([100, 200])
# print(p1.add(p2))
# print(p1 + p2)
print(p1(1))


# print(p1)
# print(p2)
# print(p3)
# print(p4)