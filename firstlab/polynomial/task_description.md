Objective: Define a Python class Polynomial which provides methods for performing algebraic operations on polynomials. Your class should behave as described in the following sample transcript:
>>> p1 = Polynomial([1, 2, 3])
>>> p1
1.000 z**2 + 2.000 z + 3.000
>>> p2 = Polynomial([100, 200])
>>> p1.add(p2)
1.000 z**2 + 102.000 z + 203.000
>>> p1 + p2
1.000 z**2 + 102.000 z + 203.000
>>> p1(1)
6.0
>>> p1(-1)
2.0
>>> (p1 + p2)(10)
1323.0
>>> p1.mul(p1)
1.000 z**4 + 4.000 z**3 + 10.000 z**2 + 12.000 z + 9.000
>>> p1 * p1
1.000 z**4 + 4.000 z**3 + 10.000 z**2 + 12.000 z + 9.000
>>> p1 * p2 + p1
100.000 z**3 + 401.000 z**2 + 702.000 z + 603.000
>>> p1.roots()
[(-1+1.4142135623730947j), (-1-1.4142135623730947j)]
>>> p2.roots()
[-2.0]
>>> p3 = Polynomial([3, 2, -1])
>>> p3.roots()
[-1.0, 0.33333333333333331]
>>> (p1 * p1).roots()
Order too high to solve for roots.