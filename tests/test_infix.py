# -*- coding: utf-8 -*-

import unittest
import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from stackevaluator import infix


class TestInfix(unittest.TestCase):

    def setUp(self):
        self.infix = infix.Infix()

    def test_replace(self):
        expression = self.infix.replace("2", "%v")
        self.assertEqual(expression, "2")
        expression = self.infix.replace("2", "%v+10*100")
        self.assertEqual(expression, "2 + 10 * 100")
        expression = self.infix.replace("2", "%v+( 10 *100)")
        self.assertEqual(expression, "2 + ( 10 * 100 )")
        expression = self.infix.replace("2", "%v+( 10 *100     )")
        self.assertEqual(expression, "2 + ( 10 * 100 )")

    def test_binaryOperators(self):
        postfix = self.infix.infix_to_postfix("2 + 3")
        self.assertEqual(postfix, "2 3 +")
        postfix = self.infix.infix_to_postfix("2 - 3")
        self.assertEqual(postfix, "2 3 -")
        postfix = self.infix.infix_to_postfix("2 * 3")
        self.assertEqual(postfix, "2 3 *")
        postfix = self.infix.infix_to_postfix("2 / 3")
        self.assertEqual(postfix, "2 3 /")

    def test_binaryOperatorsPrecedence(self):
        postfix = self.infix.infix_to_postfix("2 + 3 - 5")
        self.assertEqual(postfix, "2 3 + 5 -")
        postfix = self.infix.infix_to_postfix("2 - 3 * 5")
        self.assertEqual(postfix, "2 3 5 * -")
        postfix = self.infix.infix_to_postfix("2 * 3 / 5")
        self.assertEqual(postfix, "2 3 * 5 /")
        postfix = self.infix.infix_to_postfix("2 / 3 + 5")
        self.assertEqual(postfix, "2 3 / 5 +")
        postfix = self.infix.infix_to_postfix("1 + 2 - 3 + 4 - 5 + 6 - 7 + 8 - 9")
        self.assertEqual(postfix, "1 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 -")
        postfix = self.infix.infix_to_postfix("1 + 2 - 3 + 4 - 5 + 6 - 7 + 8 - 9 * 10")
        self.assertEqual(postfix, "1 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 10 * -")

    def test_parenthesisPrecedence(self):
        postfix = self.infix.infix_to_postfix("( 2 + 3 ) * ( 4 + 5 )")
        self.assertEqual(postfix, "2 3 + 4 5 + *")
        postfix = self.infix.infix_to_postfix("( 2 + 3 ) * 4")
        self.assertEqual(postfix, "2 3 + 4 *")
        postfix = self.infix.infix_to_postfix("2 + ( 3 * 4 )")
        self.assertEqual(postfix, "2 3 4 * +")
        postfix = self.infix.infix_to_postfix("2 + 3 * 4")
        self.assertEqual(postfix, "2 3 4 * +")
        postfix = self.infix.infix_to_postfix("( ( 2 + 3 ) * 5 ) - 10")
        self.assertEqual(postfix, "2 3 + 5 * 10 -")
        postfix = self.infix.infix_to_postfix("( ( 2 + 3 ) * 5 ) - ( - 10 )")
        self.assertEqual(postfix, "2 3 + 5 * 0 10 - -")

    def test_unaryOperators(self):
        postfix = self.infix.infix_to_postfix("( - 1 )")
        self.assertEqual(postfix, "0 1 -")
        postfix = self.infix.infix_to_postfix("- 1")
        self.assertEqual(postfix, "0 1 -")
        postfix = self.infix.infix_to_postfix("( - ( 2 * 3 ) )")
        self.assertEqual(postfix, "0 2 3 * -")
        postfix = self.infix.infix_to_postfix("- ( 2 * 3 )")
        self.assertEqual(postfix, "0 2 3 * -")
        postfix = self.infix.infix_to_postfix("1 + ( - ( 2 * 3 ) )")
        self.assertEqual(postfix, "1 0 2 3 * - +")


if __name__ == '__main__':
    unittest.main(verbosity=2)
