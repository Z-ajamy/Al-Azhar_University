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

# --- Function Evaluation ---
def evaluate_function(func_str, x):
    """
    Evaluates the function at a specific point x.
    """
    try:
        # Create a safe evaluation environment
        local_dict = {"math": math, "x": x}
        result = eval(func_str, {"__builtins__": None}, local_dict)
        if math.isnan(result) or math.isinf(result):
            raise ValueError(f"Invalid result: {result} at x={x}")
        return result
    except Exception as e:
        print(f"[Error] Could not evaluate: {e}")
        return None

# --- Get Function from User ---
def get_function():
    """
    Prompts the user to input a mathematical function.
    """
    print("\nEnter the function f(x) (use 'x' as the variable, e.g., math.sin(x) + x**2):")
    func_str = input("f(x) = ")

    # Check if the function contains 'x'
    if 'x' not in func_str:
        print("[Warning] 'x' is not found in the function string.")
    
    return func_str

# --- Bisection Method ---
def bisection_method(func_str, a, b, tolerance):
    """
    Approximate root of the function using the Bisection Method.
    """
    fa = evaluate_function(func_str, a)
    fb = evaluate_function(func_str, b)

    # Ensure the function values at the interval endpoints have opposite signs
    if fa * fb > 0:
        print("[Error] No sign change in the interval.")
        return None

    # Perform Bisection Method
    iteration = 0
    while (b - a) / 2 > tolerance:
        iteration += 1
        midpoint = (a + b) / 2
        fm = evaluate_function(func_str, midpoint)

        print(f"Iteration {iteration}: a = {a}, b = {b}, midpoint = {midpoint}, f(midpoint) = {fm}")

        if fm == 0:
            print(f"[Info] Exact root found at {midpoint}")
            return midpoint
        elif fa * fm < 0:
            b = midpoint
            fb = fm
        else:
            a = midpoint
            fa = fm

    return (a + b) / 2

# --- Main Program ---
def main():
    """
    Main program to interact with the user and apply the Bisection Method.
    """
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

    tolerance = float(input("\nEnter the tolerance (e.g., 0.0001): "))

    root = bisection_method(func_str, a, b, tolerance)
    if root is not None:
        print(f"\n[Result] Approximate root: {root}")
    else:
        print("[Error] Root not found.")

if __name__ == "__main__":
    print("Name: Abd Al-rahman Ahmed Mohammed Mahmoud\nID: 20211048")
    
    try:
        print("=" * 80)
        print("Welcome to the Modified Bisection’s Method Solver")
        print("=" * 80)
        print("Choose an option:")
        print("1 - Solve a function using Bisection's Method")
        print("2 - Display input function documentation")
        print("0 - Exit")
        print("-" * 80)

        choice = input("> ").strip()

        if choice == "1":
            main()
        elif choice == "2":
            print(__doc__)
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
