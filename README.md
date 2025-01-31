# Numerical Methods Implementation

- Approximation Algorithm
- Bisection Method
- Fixed-Point Iteration
- Newton-Raphson Method

### Installation Instruction:

1. Download assignment_1.py and run in VsCode, compare with output.txt

2. If you want to check test_assignment_1.py (pretty much the same as assignment_1.py):
   - Download and put test_assignment_1.py in the folder containing assignment_1
   - Change ```from ..main.assignment_1 import``` to ```from assignment_1 import```
   - Install required library (pytest)

### Available Methods

1. **Approximation Algorithm**
   - Input: Initial guess (x0) and tolerance
   - Usage: `approximation_algorithm(1.5, 0.000001)`

2. **Bisection Method**
   - Input: Tolerance, left bound, right bound, maximum iterations
   - Usage: `bisection_method(0.001, 1, 2, 50)`

3. **Fixed-Point Iteration**
   - Input: Initial guess (p0), tolerance, maximum iterations
   - Usage: `fixed_point_iteration(1.5, 0.000001, 50)`

4. **Newton-Raphson Method**
   - Input: Initial guess, tolerance, maximum iterations
   - Usage: `newton_raphson(math.pi/4, 0.000001, 50)`

## Equations Used in Methods

### Approximation Algorithm
x = (x/2) + (1/x)

### Bisection Method
x³ + 4x² - 10

### Fixed-Point Iteration
Equation 1: x³ + 4x² - 10 (default, change to use equation 2 if needed).
Equation 2:  sqrt(10 - x³) / 2.

### Newton-Raphson Method
cos(x) = x.

## Author
Duc Nguyen
