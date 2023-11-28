import re
import unittest
from parameterized import parameterized

# The class containing the test cases
class TestStringMethods(unittest.TestCase):
    singleExpressionPattern = r'^(?P<operator><|>|<>|!=|=!|==|<=|>=|=)(?P<value>\d+(\.\d+)?)$'
    expressions = [
        ">100",
        "<100",
        "<>100",
        "!=100",
        "=100",
        "<=100",
        ">=100",
        ">100.1",
        "<100.1",
        "<>100.1",
        "!=100.1",
        "=100.1",
        "<=100.1",
        ">=100.1",
        # ">100|<=200",
        # "<>150&!=300",
        # "<100|>=500|<=700",
        # "<100|>=100.5&<=200.7",
    ]

    @parameterized.expand([
        (">100", ">", "100"),
        ("<100", "<", "100"),
        ("<>100", "<>", "100"),
        ("=100", "=", "100"),
        ("==100", "==", "100"),
        ("!=100", "!=", "100"),
        ("=!100", "=!", "100"),
        ("<=100", "<=", "100"),
        (">=100", ">=", "100"),
        (">100.1", ">", "100.1"),
        ("<100.1", "<", "100.1"),
        ("<>100.1", "<>", "100.1"),
        ("=100.1", "=", "100.1"),
        ("==100.1", "==", "100.1"),
        ("!=100.1", "!=", "100.1"),
        ("=!100.1", "=!", "100.1"),
        ("<=100.1", "<=", "100.1"),
        (">=100.1", ">=", "100.1"),
    ])
    def test_single_expression_should_match(self, exp, expectedSign, expectedValue):
        match = re.match(self.singleExpressionPattern, exp)
        self.assertIsNotNone(match)
        self.assertEqual(match.group('operator'), expectedSign, expectedSign + " >>>> FAILED")
        self.assertEqual(match.group('value'), expectedValue, expectedSign + " >>>> FAILED")

    @parameterized.expand([
        ("!<100"),
        ("!>100"),
        (">!100"),
        ("<!100"),
        ("=<100"),
        ("=>100"),
        ("><100")
    ])
    def test_single_expression_should_not_match(self, exp):
        match = re.match(self.singleExpressionPattern, exp)
        self.assertIsNone(match)

if __name__ == '__main__':
    unittest.main()
