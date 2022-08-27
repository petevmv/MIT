import unittest
from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    def test_build_visual_of_equasion(self):
        tests_for_visual_of_eq = [(0, ""), (1, "z"), (2, "z**2"), (3, "z**3")]
        for element, expected in tests_for_visual_of_eq:
            with self.subTest(f"{element} was given, expected result {expected}"):
                self.assertEqual(Polynomial.build_visual_of_equation(element), expected)

    def test_val(self):
        tests_equation_val_expected = [
            ([1, 2, 3], 2, 11),
            ([2, 3, 4], 3, 31),
            ([2, 4], 5, 14),
            ([1, 2, 3, 4], 3, 58),
        ]
        for polynom, value, expected in tests_equation_val_expected:
            with self.subTest(f"{Polynomial(polynom)} / z={value} ==> {expected}"):
                self.assertEqual(Polynomial(polynom).val(value), expected)

    def test_roots(self):
        test_roots = [
            ([1, 2, 3], [-1 + 1j, -1 - 1j]),
            ([100, 200], [-2.0]),
            ([1, 8, 16], [-4.0]),
            ([3, 2, -1], [0.3333333333333333, -1.0]),
            ([1, 2, 3, 4, 5, 6, 7, 8], "Order too high to solve for roots"),
        ]
        for coeff, expected in test_roots:
            with self.subTest(f"{Polynomial(coeff)} roots are {expected}"):
                self.assertEqual(Polynomial(coeff).roots(), expected)

    def test_add(self):
        tests_for_add = [
            ([1, 2, 3], [100, 200], "1z**2 + 102z + 203"),
            ([1, 2, 3], [2, 3, 4], "3z**2 + 5z + 7"),
            ([4, 5, 6, 7], [6, 10], "4z**3 + 5z**2 + 12z + 17"),
            ([10, 11, 12, 1, 2], [2, 3, 5], "10z**4 + 11z**3 + 14z**2 + 4z + 7"),
        ]
        for p1, p2, expected in tests_for_add:
            with self.subTest(
                f"sum of {Polynomial(p1)} and {Polynomial(p2)} should be {expected}"
            ):
                self.assertEqual(f"{Polynomial(p1) + Polynomial(p2)}", expected)


if __name__ == "__main__":
    unittest.main()

