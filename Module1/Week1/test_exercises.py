import unittest
from unittest.mock import patch
from Exercises import exercise1, is_number, exercise2, calc_ae, calc_se, factorial
from Exercises import approx_cos, approx_cosh, approx_sin, approx_sinh


class test_exercise(unittest.TestCase):
    def test_calc_f1_score(self):
        self.assertAlmostEqual(
            exercise1(tp=2, fp=3, fn=5), 0.33, places=2
        )
    
    def test_calc_f1_score_2(self):
        self.assertEqual(
            exercise1(-1, 1, 1), -1
        )

    def test_is_number(self):
        self.assertTrue(is_number(3))
        self.assertFalse(is_number('-2a'))


    

    @patch('builtins.input', side_effect=['3', 'sigmoid'])
    def test_sigmoid(self, mock_input):
        result = exercise2()
        self.assertAlmostEqual(
            result, 0.95, places=2
        )

    @patch('builtins.input', side_effect=['1', 'elu'])
    def test_elu(self, mock_input):
        result = exercise2()
        self.assertEqual(
            result, 1
        )

    @patch('builtins.input', side_effect=['2', 'relu'])
    def test_relu_function(self, mock_input):
        result = exercise2()
        self.assertEqual(
            result, 2
        )

    def test_calc_ae(self):
        self.assertEqual(
            calc_ae(1, 6), 5
        )

    def test_calc_se(self):
        self.assertEqual(
            calc_se(4, 2), 4
        )

    def test_factorial(self):
        self.assertEqual(
            factorial(5), 120
        )

    def test_approx_cos(self):
        self.assertAlmostEqual(
            approx_cos(x=1, n=10), 0.54, places=2
        )

    def test_approx_sin(self):
        self.assertAlmostEqual(
            approx_sin(x=1, n=10), 0.8415, places=4
        )

    def test_approx_sinh(self):
        self.assertAlmostEqual(
            approx_sinh(x=1, n=10), 1.18, places=2
        )

    def test_approx_cosh(self):
        self.assertAlmostEqual(
            approx_cosh(x=1, n=10), 1.54, places=2
        )
    



if __name__ == "__main__":
    unittest.main()
