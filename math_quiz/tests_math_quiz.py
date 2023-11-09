import unittest
from math_quiz import generateRandomInteger, selectRandomArithmetic, calculateMathematicalExpression


class TestMathGame(unittest.TestCase):

    def test_generateRandomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10

        # Test a large number of random values
        for _ in range(10000):
            rand_num = generateRandomInteger(min_val, max_val)

            # Check if the random number is within the specified range
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_selectRandomArithmetic(self):
        # Test if the selected operator is one of the expected arithmetic operators
        expected_operators = ['+', '-', '*']

        # Test a large number of random values
        for _ in range(10000):
            operator = selectRandomArithmetic()

            # Check if the selected operator is one of the expected operators
            self.assertIn(operator, expected_operators)

    def test_calculateMathematicalExpression(self):
        # Define test cases
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 4, '-', '7 - 4', 3),
            (2, 8, '*', '2 * 8', 16),
            (2, 0, '*', '2 * 0', 0),
            (0, 3, '+', '0 + 3', 3)
        ]
        # Iterate through the test cases
        for num1, num2, operator, expected_problem, expected_answer in test_cases:

            # Obtain the problem and calculate the answer using the function to be tested
            problem, answer = calculateMathematicalExpression(num1, num2, operator)

            # Check if the calculated problem matches the expected problem
            self.assertEqual(problem, expected_problem)
            # Check if the calculated answer matches the expected answer
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
