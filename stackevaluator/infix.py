# -*- coding: utf-8 -*-

from .stack import Stack
import re


class Infix:

    PRECEDENCE = {}
    PRECEDENCE["*"] = 3
    PRECEDENCE["/"] = 3
    PRECEDENCE["+"] = 2
    PRECEDENCE["-"] = 2
    PRECEDENCE["("] = 1
    UNARY_OPERATORS = "-"
    BINARY_OPERATORS = "+*/"
    OPERATORS = BINARY_OPERATORS + UNARY_OPERATORS
    OPERANDS = "(\d+(\.\d+)?)"   # Integers and floats with 0123456789.
    EXTRA_SPACES = "( )( )+"
    numbers_pattern = re.compile(OPERANDS)
    spaces_pattern = re.compile(EXTRA_SPACES)

    def __init__(self, calibration=None):
        self.calibration = calibration

    def replace(self, value, expression):

        for operator in self.OPERATORS:
            expression = expression.replace(operator, " " + operator + " ")
        expression = expression.replace("(", "( ")
        expression = expression.replace(")", " )")
        expression = re.sub(self.spaces_pattern, " ", expression)   # Remove extra spaces by only one
        expression = expression.strip()
        if expression[0] in self.OPERATORS and "%v" not in expression:
            return value + " " + expression
        else:
            return expression.replace("%v", value)

    def infix_to_postfix(self, infix_expression):
        postfix_expression = []
        infix_tokenList = infix_expression.split(" ")
        stack = Stack()

        if infix_tokenList[-1] in self.OPERATORS:
            error = "InFix invalid expression: Missing operand at the end! --> " + infix_expression + " _?_"
            print(error)
            return [None, error]

        last_token = ""
        for token in infix_tokenList:
            if self.numbers_pattern.match(token):
                postfix_expression.append(token)
            elif token == '(':
                stack.push(token)
            elif token == ')':
                while not stack.isEmpty() and stack.peek() != '(':
                    postfix_expression.append(stack.pop())
                try:
                    stack.pop()
                except IndexError as e:
                    error = "InFix invalid expression: Mismatched parentheses! --> Missing at least one \"(\" or there is at least one extra \")\""
                    print(error)
                    return [None, error]
            elif token in self.OPERATORS:
                if stack.isEmpty() or stack.peek() == '(':
                    if token in self.UNARY_OPERATORS \
                            and not self.numbers_pattern.match(last_token) and last_token != ')':
                        postfix_expression.append('0')
                    stack.push(token)
                else:
                    try:
                        while not stack.isEmpty() and self.PRECEDENCE[token] <= self.PRECEDENCE[stack.peek()]:
                            postfix_expression.append(stack.pop())
                    except KeyError as e:
                        error = "InFix invalid expression: 2 or more consecutive operators!"
                        print(error)
                        return [None, error]
                    stack.push(token)

            last_token = token

        while not stack.isEmpty():
            if stack.peek() == "(":
                error = "InFix invalid expression: Mismatched parentheses! --> Missing at least one \")\" or there is at least one extra \"(\""
                print(error)
                return [None, error]
            else:
                postfix_expression.append(stack.pop())

        return " ".join(postfix_expression)
