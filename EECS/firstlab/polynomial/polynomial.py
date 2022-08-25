# from collections import defaultdict


class Polynomial:

    # създаване на у-то
    # ако коефициента = 0 -> кореспондиращата позиция с него не участва в състава
    # степента на у-то зависи от броя на елементи в списъка минус 1
    # (5 елемента -> у-е от 4та степен)
    #
    def __init__(self, coefficients):
        self.equation = ""
        self.coefficients = coefficients
        self.degree = len(coefficients) - 1

    def build_visual_of_equation(degree):
        equation = ""

        if degree == 0:
            equation = ""

        elif degree == 1:
            equation = "z"

        else:
            equation = f"z**{degree}"

        return equation

    def val(self, value):
        result = [
            x * value ** (self.degree - idx) for idx, x in enumerate(self.coefficients)
        ]
        return sum(result)

    def __call__(self, x):
        return self.val(x)

    def roots(self):
        # compute roots of the equation
        if self.degree > 2:
            return "Order too high to solve for roots"
        if self.degree == 2:
            a, b, c = self.coefficients
            D = b ** 2 - 4 * a * c
            x1 = (-b + D ** 0.5) / (2 * a)
            x2 = (-b - D ** 0.5) / (2 * a)
            if D == 0:
                return [-b / (2 * a)]
            if D > 0:
                return [x1, x2]

            complex_roots = (
                complex(round(x1.real), round(x1.imag)),
                complex(round(x2.real), round(x2.imag)),
            )
            return [complex_roots[0], complex_roots[1]]

        elif self.degree == 1:
            a, b = self.coefficients
            x1 = -b / a
            return [x1]

    def add(self, other):
        p1 = self.coefficients
        p2 = other.coefficients
        if len(self.coefficients) < len(other.coefficients):
            p1 = [0] * (len(other.coefficients) - len(self.coefficients)) + p1
        if len(self.coefficients) > len(other.coefficients):
            p2 = [0] * (len(self.coefficients) - len(other.coefficients)) + p2
            # print(p2)
        element_wise = [x + y for x, y in zip(p1, p2)]
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
        pow = 0
        product = {}
        for i, j in enumerate(p1):
            for I, J in enumerate(p2):
                pow = i + I
                if order_p1 + order_p2 - pow not in product:
                    product[order_p1 + order_p2 - pow] = j * J
                else:
                    product[order_p1 + order_p2 - pow] += j * J
        result = []

        for order, coeff in product.items():
            result.append(coeff)

        # print(p1,order_p1, p2, order_p2)

        # tup_p1 = []
        # tup_p2 = []

        # for i in p1:
        # 	tup_p1.append((i, order_p1))
        # 	order_p1 -= 1
        # for i in p2:
        # 	tup_p2.append((i, order_p2))
        # 	order_p2 -= 1
        # tup_of_coeff_and_power = []
        # for x in tup_p1:
        # 	for y in tup_p2:
        # 		tup_of_coeff_and_power.append((x[0] * y[0], x[1] + y[1]))
        # # print(tup_of_coeff_and_power)

        # # This block of code will add all coeffs of the same order
        # d = defaultdict(float)

        # for x, y in tup_of_coeff_and_power:
        # 	d[y] += float(x)

        # # returning to list structure to pass it to polynomial class
        # result = []
        # for x in d.items():
        # 	result.append(x[1])

        return Polynomial(result)

    def __mul__(self, p):
        return self.mul(p)

    def __str__(self):
        equation = ""

        for idx, el in enumerate(self.coefficients):

            if el == 0:
                continue

            if el > 0:
                sing = "+"

            else:
                sing = "-"

            equation = (
                equation
                + f" {self.coefficients[idx]}{Polynomial.build_visual_of_equation(self.degree - idx)} {sing}"
            )

        return equation.rstrip("+").strip()

    def __repr__(self):
        return str(tuple(self.coefficients))


# p1 = Polynomial([-1, 2, -3, 4])
# p2 = Polynomial([3, 4, 5])
# p3 = Polynomial([-10, 2, 1])
# p4 = Polynomial([1, 2, 0, 4])

p1 = Polynomial([1, 2, 3])
p2 = Polynomial([100, 200])
p3 = Polynomial([3, 2, -1])
p4 = Polynomial([1, 8, 16])

# print(p1.add(p2))
# print((p1 + p2)(10))
# print(p1(-1))
# print(p1.mul(2))
print(p1.roots())
print(p2.roots())
print(p3.roots())
print(p4.roots())
print((p1 * p2).roots())
