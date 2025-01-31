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
   - Install required library (pytest):
```bash
pip install -r requirements.txt
```

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

## Testing

Run the tests using pytest:

```bash
pytest src/test/test_assignment_1.py
```

## Method Details

### Approximation Algorithm
Iteratively approximates the square root of a number using the formula: x = (x/2) + (1/x)

### Bisection Method
Finds a root of the equation x³ + 4x² - 10 = 0 in a given interval using the bisection method.

### Fixed-Point Iteration
Uses fixed-point iteration to solve the equation 1: x³ + 4x² - 10 = 0.
Or to solve the equation 2:  sqrt(10 - x³) / 2.

### Newton-Raphson Method
Implements the Newton-Raphson method to find a root of the equation cos(x) = x.

## Author
[Duc Nguyen]
