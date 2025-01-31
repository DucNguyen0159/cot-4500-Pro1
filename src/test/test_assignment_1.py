import pytest
from ..main.assignment_1 import (
    approximation_algorithm,
    bisection_method,
    fixed_point_iteration,
    newton_raphson
)
import math

def test_approximation_algorithm():
    # Test with known value
    x0 = 1.5
    tol = 0.000001
    # Capture the output to verify it runs without errors
    approximation_algorithm(x0, tol)
    # You might want to modify the function to return the final value
    # and then assert it's close to the expected result

def test_bisection_method():
    tol = 0.001
    left = 1
    right = 2
    max_iter = 50
    # Test with known interval
    bisection_method(tol, left, right, max_iter)
    # Similarly, you might want to modify the function to return the result
    # and assert it's within the expected range

def test_fixed_point_iteration():
    p0 = 1.5
    tol = 0.000001
    N0 = 50
    # Test with known initial guess
    fixed_point_iteration(p0, tol, N0)
    # You could modify the function to return the final value
    # and verify it satisfies the fixed point equation

def test_newton_raphson():
    p_prev = math.pi / 4
    tol = 0.000001
    N0 = 50
    # Test with known starting point
    newton_raphson(p_prev, tol, N0)
    # Could modify to return final value and verify it's close to
    # the actual solution of cos(x) = x

# Additional test cases for edge cases
def test_bisection_method_small_interval():
    tol = 0.001
    left = 1.5
    right = 1.6
    max_iter = 50
    bisection_method(tol, left, right, max_iter)

def test_newton_raphson_bad_initial_guess():
    p_prev = 10  # A deliberately poor initial guess
    tol = 0.000001
    N0 = 50
    newton_raphson(p_prev, tol, N0)
