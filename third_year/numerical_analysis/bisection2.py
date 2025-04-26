"""
================================================================================
Function Input Guidelines for Bisection Method Solver
================================================================================

This program accepts a mathematical function as a string input (e.g., "math.sin(x) + x**2")
and evaluates it numerically using Python's built-in `eval()` function.

To ensure safety and correctness, the evaluation environment is restricted to:
    - No access to built-in functions (for security)
    - Access only to:
        • math module (e.g., math.sin, math.exp, math.sqrt, math.log, etc.)
        • the variable 'x' (the point at which the function is evaluated)

--------------------------------------------------------------------------------
SUPPORTED FUNCTION TYPES:
--------------------------------------------------------------------------------
1. ALGEBRAIC FUNCTIONS:
    • Polynomials:        x**2 - 3*x + 7
    • Rational forms:     (x**2 + 1) / (x - 2)
    • Roots:              math.sqrt(x), x**(1/3)

2. TRIGONOMETRIC FUNCTIONS:
    • Sine/Cosine/Tangent:    math.sin(x), math.cos(x), math.tan(x)
    • Inverse trig:           math.asin(x), math.acos(x), math.atan(x)

3. EXPONENTIAL & LOGARITHMIC:
    • Exponential:            math.exp(x)
    • Natural log (ln):       math.log(x)
    • Log base 10:            math.log10(x)

4. CONSTANTS:
    • Pi:                     math.pi
    • Euler's number (e):     math.e

--------------------------------------------------------------------------------
UNSUPPORTED OR DANGEROUS INPUTS:
--------------------------------------------------------------------------------
Do NOT use 'abs(x)'  Use 'math.fabs(x)' instead.
Do NOT use 'sin(x)'  Use 'math.sin(x)' instead.
Do NOT use '^' for exponentiation  Use '**'.
Do NOT write 'e^x'  Use 'math.exp(x)'.
Do NOT write 'ln(x)'  Use 'math.log(x)'.
--------------------------------------------------------------------------------
EXAMPLES OF VALID INPUT:
    • math.sin(x) + x**2
    • math.exp(x) - 5
    • math.sqrt(x) - 3
    • x**3 - 4*x + 1
    • math.log(x + 10)
================================================================================
"""

import math

def evaluate_function(func_str, x):
    return eval(func_str, {}, {"x": x, "math": math})

def get_function():

    print("\nEnter the function f(x) (use 'x' as the variable, like:- math.sin(x) + x**2):")
    func_str = input("f(x) = ")

    # Check if the function have x
    if 'x' not in func_str:
        print("[Warning] 'x' is not found in the function string.")
    
    return func_str

def bisection_method(func_str, a, b, stop):
    
    fa = evaluate_function(func_str, a)
    fb = evaluate_function(func_str, b)

    if fa * fb > 0:
        print("[Error] No sign change in the interval.")
        return None

    try:
        max_iterations = math.ceil((math.log(b - a) - math.log(stop)) / math.log(2))
    except ValueError:
        print("[Error] Invalid interval or stop for logarithmic computation.")
        return None

    print(f"[Info] Estimated max iterations: {max_iterations}")

    for iteration in range(1, max_iterations + 1):
        midpoint = (a + b) / 2
        fm = evaluate_function(func_str, midpoint)

        print(f"Iteration {iteration}: a = {a}, b = {b}, midpoint = {midpoint}, f(midpoint) = {fm}")

        if fm == 0:
            print(f"[Info] root found at {midpoint}")
            return midpoint
        elif fa * fm < 0:
            b = midpoint
            fb = fm
        else:
            a = midpoint
            fa = fm

    return (a + b) / 2

def main():

    print("=" * 50)
    print("Bisection Method Root Finder")
    print("=" * 50)

    func_str = get_function()
    if func_str is None:
        return

    try:
        a = float(input("\nEnter the start of the interval (a): "))
        b = float(input("Enter the end of the interval (b): "))
    except ValueError:
        print("[Error] Invalid input for interval.")
        return

    stop = float(input("\nEnter the stop (e.g., 0.0001): "))

    root = bisection_method(func_str, a, b, stop)
    if root is not None:
        print(f"\n[Result] Approximate root: {root}")
    else:
        print("[Error] Root not found.")

if __name__ == "__main__":
    print("Name: Abd Al-rahman Ahmed Mohammed Mahmoud\nID: 20211048")
    
    print("=" * 80)
    print("Welcome to the Bisection’s Method Solver")
    print("=" * 80)
    print("Choose an option:")
    print("1 - Solve a function using Bisection's Method")
    print("2 - Display input function documentation")
    print("0 - Exit")
    print("-" * 80)

    choice = input("> ")

    if choice == "1":
        main()
    elif choice == "2":
        print(__doc__)
    elif choice == "0":
        print("Exiting the program. Goodbye!")
        exit(0)
    else:
        print("Invalid choice. Please enter 1, 2, or 0.")
