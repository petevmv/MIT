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


if __name__ == "__main__":
    unittest.main()

