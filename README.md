# Numerical Methods Implementation

- Approximation Algorithm
- Bisection Method
- Fixed-Point Iteration
- Newton-Raphson Method

### Installation Instruction:

1. Clone the repository:
```bash
git clone <your-repository-url>
```

2. Navigate to the project directory:
```bash
cd <project-directory>
```

3. Install required dependencies:
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
