import unittest
from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    def test_build_visual_of_equasion(self):
        tests_for_visual_of_eq = [(0, "",), (1, "z"), (2, "z**2",), (3, "z**3")]
        for element, expected in tests_for_visual_of_eq:
            with self.subTest(f"{element} was given, expected result {expected}"):
                self.assertEqual(Polynomial.build_visual_of_equation(element), expected)


if __name__ == "__main__":
    unittest.main()

