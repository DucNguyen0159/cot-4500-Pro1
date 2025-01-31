import pytest
from ..main.assignment_1 import (
    approximation_algorithm,
    bisection_method,
    fixed_point_iteration,
    newton_raphson
)
import math

def test_approximation_algorithm():
    x0 = 1.5
    tol = 0.000001
    approximation_algorithm(x0, tol)

def test_bisection_method():
    tol = 0.001
    left = 1
    right = 2
    max_iter = 50
    bisection_method(tol, left, right, max_iter)

def test_fixed_point_iteration():
    p0 = 1.5
    tol = 0.000001
    N0 = 50
    fixed_point_iteration(p0, tol, N0)

def test_newton_raphson():
    p_prev = math.pi / 4
    tol = 0.000001
    N0 = 50
    newton_raphson(p_prev, tol, N0)

if __name__ == "__main__":
    test_approximation_algorithm()
    test_bisection_method()
    test_fixed_point_iteration()
    test_newton_raphson()
