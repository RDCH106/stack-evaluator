# -*- coding: utf-8 -*-

import unittest
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


if __name__ == '__main__':
    unittest.main(verbosity=2)
