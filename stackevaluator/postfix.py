# -*- coding: utf-8 -*-

from __future__ import division
from .stack import Stack
import re


class Postfix:

    UNARY_OPERATORS = "-"
    BINARY_OPERATORS = "+*/"
    OPERATORS = BINARY_OPERATORS + UNARY_OPERATORS
    OPERANDS = "(\d+(\.\d+)?)"  # Integers and floats with 0123456789.

    numbers_pattern = re.compile(OPERANDS)

    def eval(self, operator, operandA, operandB):
        for op in self.OPERATORS:
            if op == operator:
                expression = operandB + op + operandA
                return str(eval(expression))

    def postfix_eval(self, postfix_expression):
        if not postfix_expression:
            return None
        postfix_tokenList = postfix_expression.split(" ")
        stack = Stack()

        for token in postfix_tokenList:
            if self.numbers_pattern.match(token):
                stack.push(token)
            else:
                operandA = stack.pop()
                try:
                    operandB = stack.pop()
                except IndexError as e:
                    error = "PostFix invalid expression: 2 or more consecutive operators!"
                    print(error)
                    return [None, error]
                result = self.eval(token, operandA, operandB)
                stack.push(result)

        result = stack.pop()
        if stack.isEmpty():
            return result
        else:
            error = "PostFix invalid expression"
            return [None, error]
