class Polynomial:
	# създаване на у-то
	# ако коефициента = 0 -> кореспондиращата позиция с него не участва в състава
	# степента на у-то зависи от броя на елементи в списъка минус 1 
	# (5 елемента -> у-е от 4та степен) 
	# 
	def __init__(self, coefficients):
		self.eq = ''
		self.coefficients = coefficients
		self.degree = len(coefficients) - 1
		

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
			eq = ''
			
			if degree == 0:
				eq = ''
			
			elif degree == 1:
				eq = 'z'
			
			else:
				eq = f'z**{degree}'
			
			return eq


	def __str__(self):
		eq = ''
		
		for idx, el in enumerate(self.coefficients):
			
			if el == 0:
				continue
			
			if el > 0:
				sing = '+'
			
			else: 
				sing = '-'
			
			eq = eq + f" {self.coefficients[idx]}{Polynomial.expr_x(len(self.coefficients) - idx - 1)} {sing}"

		return eq.rstrip('+').strip()
	
	def __repr__(self):
		return str(tuple(self.coefficients))


# p1 = Polynomial([-1, 2, -3, 4])
# p2 = Polynomial([3, 4, 5])
# p3 = Polynomial([-10, 2, 1])
# p4 = Polynomial([1, 2, 0, 4])

p1 = Polynomial([1,2,3])
p2 = Polynomial([100, 200])
print(p1.add(p2))
print(p1 + p2)


# print(p1)
# print(p2)
# print(p3)
# print(p4)