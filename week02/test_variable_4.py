from math import sqrt
from unittest import TestCase

def test_variable_4():
    import lab_variable_4
    a = 5.0
    b = -22.0
    c = 8.0
    x1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
    answer = [x1, x2]
    answer.sort()
    r1, r2 = lab_variable_4.quad_formula(a, b, c)
    result = [r1, r2]
    result.sort()
    a = TestCase()
    a.assertListEqual(answer, result)