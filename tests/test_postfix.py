import unittest
import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from stackevaluator import postfix


class TestPostfix(unittest.TestCase):

    def setUp(self):
        self.postfix = postfix.Postfix()

    def test_binaryOperators(self):
        result = self.postfix.postfix_eval("2 3 +")
        self.assertEqual(result, "5")
        result = self.postfix.postfix_eval("2 3 -")
        self.assertEqual(result, "-1")
        result = self.postfix.postfix_eval("2 3 *")
        self.assertEqual(result, "6")
        result = self.postfix.postfix_eval("2 3 /")
        self.assertEqual(result[0:12], "0.6666666666")

    def test_binaryOperatorsPrecedence(self):
        result = self.postfix.postfix_eval("2 3 + 5 -")
        self.assertEqual(result, "0")
        result = self.postfix.postfix_eval("2 3 5 * -")
        self.assertEqual(result, "-13")
        result = self.postfix.postfix_eval("2 3 * 5 /")
        self.assertEqual(result, "1.2")
        result = self.postfix.postfix_eval("2 3 / 5 +")
        self.assertEqual(result[0:12], "5.6666666666")
        result = self.postfix.postfix_eval("1 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 -")
        self.assertEqual(result, "-3")
        result = self.postfix.postfix_eval("1 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 10 * -")
        self.assertEqual(result, "-84")


if __name__ == '__main__':
    unittest.main(verbosity=2)
