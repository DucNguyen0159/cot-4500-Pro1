import math

def approximation_algorithm(x0, tol):
    print("*** Approximation Algorithm ***")
    
    iter = 0
    diff = x0
    x = x0
    
    print(f"{iter} : {x}")
    
    while diff >= tol:
        iter += 1
        y = x
        x = (x / 2) + (1 / x)
        print(f"{iter} : {x}")
        diff = abs(x - y)
    
    print(f"\nConvergence after {iter} iterations")

def bisection_method(tol, left, right, max_iter):
    print("\n*** The Bisection Method ***")
    
    p = 0
    i = 0
    
    while abs(right - left) > tol and i < max_iter:
        i += 1
        p = (left + right) / 2
        print(f"{i} : {p}")
        
        fleft = left**3 + 4 * left**2 - 10
        fp = p**3 + 4 * p**2 - 10
        
        if (fleft < 0 and fp > 0) or (fleft > 0 and fp < 0):
            right = p
        else:
            left = p
    
    print(f"\np = {p}")
    print(f"{i} iterations are sufficient.")

def fixed_point_iteration(p0, tol, N0):
    print("\n*** The Fixed-Point Iteration ***")
    
    result = "Failure"
    i = 1
    p = 0
    
    while i <= N0:
        p = p0 - p0 * p0 * p0 - 4 * p0 * p0 + 10  # Equation 1
        # p = math.sqrt(10 - p0 * p0 * p0) / 2  # Equation 2
        
        if math.isnan(p):
            print("\nResult diverges")
            break
        
        print(f"{i} : {p}")
        
        if abs(p - p0) < tol:
            result = "Success"
            break
        
        i += 1
        p0 = p
    
    print(f"\n{result} after {i} iterations\n")

def newton_raphson(p_prev, tol, N0):
    print("\n*** The Newton-Raphson Method ***")
    
    i = 1
    print(f"{i} : {p_prev}")
    
    while i <= N0:
        fp_prev = math.cos(p_prev) - p_prev
        fp1_prev = -math.sin(p_prev) - 1
        
        if fp1_prev != 0:
            p_next = p_prev - fp_prev / fp1_prev
            
            if abs(p_next - p_prev) < tol:
                print(f"\np_next = {p_next}\nSuccess")
                break
            
            i += 1
            p_prev = p_next
            print(f"{i} : {p_prev}")
        else:
            print("Unsuccessful (Derivative is zero)")
            break
    
    if i > N0:
        print("Max iterations performed.")

if __name__ == "__main__":
    approximation_algorithm(1.5, 0.000001)
    bisection_method(0.001, 1, 2, 50)
    fixed_point_iteration(1.5, 0.000001, 50)
    newton_raphson(math.pi / 4, 0.000001, 50)

