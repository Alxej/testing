import unittest
from root import calculate_cuadratic_roots


class TestNegativeEquatation(unittest.TestCase):

    def test_incorrect_a_type(self):
        a_incorrect_values = ['10', '3.0', 'asda', True, [], {}]
        b = 4
        c = 5
        for a in a_incorrect_values:
            with self.assertRaises(TypeError):
                calculate_cuadratic_roots(a, b, c)

    def test_incorrect_b_type(self):
        a = 4
        b_incorrect_values = ['10', '3.0', 'asda', True, [], {}]
        c = 5
        for b in b_incorrect_values:
            with self.assertRaises(TypeError):
                calculate_cuadratic_roots(a, b, c)

    def test_incorrect_c_type(self):
        a = 4
        b = 5
        c_incorrect_values = ['10', '3.0', 'asda', True, [], {}]
        for c in c_incorrect_values:
            with self.assertRaises(TypeError):
                calculate_cuadratic_roots(a, b, c)

    def test_not_quadratic_eqatation(self):
        a = 0
        b = 4
        c = 5

        with self.assertRaises(ValueError):
            calculate_cuadratic_roots(a, b, c)


class TestPositiveEquatation(unittest.TestCase):

    def test_two_roots(self):
        a = 1
        b = -5
        c = 6

        roots = calculate_cuadratic_roots(a, b, c)

        self.assertIn(3.0, roots)
        self.assertEqual(2.0 in roots, True)

    def test_one_root(self):
        a = 1
        b = -6
        c = 9

        roots = calculate_cuadratic_roots(a, b, c)

        self.assertEqual(roots[0], roots[1])
        self.assertEqual(roots[0], 3.0)

    def test_zero_roots(self):
        a = 2
        b = 1
        c = 1

        self.assertEqual(calculate_cuadratic_roots(a, b, c), None)


class TestBorderEquatation(unittest.TestCase):

    def test_b_and_c_are_zero(self):
        a = -4
        result = calculate_cuadratic_roots(a, 0, 0)
        self.assertEqual(result, (0, 0))


if __name__ == "__main__":
    unittest.main()
