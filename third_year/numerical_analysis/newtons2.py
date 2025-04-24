
"""
================================================================================
Function Input Guidelines for Modified Newton's Method Solver
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

# ---------------------------------------
# Evaluate the user-defined function at point x
# ---------------------------------------
def evaluate(func_str, x):
    try:
        return eval(func_str, {"__builtins__": None, "math": math, "x": x})
    except Exception as e:
        raise ValueError(f"Error while evaluating the function: {e}")

# ------------------------------------------------
# Numerical derivative using central difference method
# ------------------------------------------------
def derivative(func_str, x, h=1e-6):
    f_x_plus = evaluate(func_str, x + h)
    f_x_minus = evaluate(func_str, x - h)
    return (f_x_plus - f_x_minus) / (2 * h)

# ------------------------------------------------
# Format a number in base-10 exponential form: a × 10^b
# ------------------------------------------------
def format_power_of_ten(number):
    if number == 0:
        return "0"
    exponent = int(math.floor(math.log10(abs(number))))
    base = number / (10 ** exponent)
    return f"{base:.2f} × 10^{exponent}"

# ---------------------------------------
# Modified Newton’s Method
# ---------------------------------------
def modified_newton(func_str, x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f_x = evaluate(func_str, x0)
        f_prime = derivative(func_str, x0)

        if abs(f_prime) < 1e-12:
            print("Derivative is too close to zero. Division by zero may occur.")
            return None

        x1 = x0 - f_x / f_prime

        print(f"Iteration {i+1}: x = {x1:.10f}, f(x) = {format_power_of_ten(f_x)}")

        if abs(x1 - x0) < tol or abs(f_x) < tol:
            print("\nRoot approximation has converged.")
            return x1

        x0 = x1

    print("\nMaximum iterations reached without convergence.")
    return None

# ---------------------------------------
# Main user interface
# ---------------------------------------
def main():
    print("Modified Newton’s Method for Root Finding\n")

    func_str = input("Enter the function (example: math.sin(x) - x/2):\n> ")

    # Test the function
    try:
        test_val = evaluate(func_str, 1.0)
    except Exception as e:
        print("Invalid function expression. Please check your syntax.")
        return

    try:
        a = float(input("Enter interval start (a):\n> "))
        b = float(input("Enter interval end (b):\n> "))

        f_a = evaluate(func_str, a)
        f_b = evaluate(func_str, b)

        if f_a * f_b > 0:
            print("No sign change in the interval. Cannot guarantee a root.")
            return

        x0 = (a + b) / 2
        print(f"Initial guess automatically chosen as midpoint: x0 = {x0:.10f}")

        tol_power = int(input("Enter desired accuracy power (e.g., 6 means 10^-6):\n> "))
        tol = 10 ** (-tol_power)

    except Exception as e:
        print("Invalid input or evaluation error.")
        return

    root = modified_newton(func_str, x0, tol)

    if root is not None:
        print(f"\nApproximate root: {root:.10f}")

# ---------------------------------------
# Run the program
# ---------------------------------------

if __name__ == "__main__":
    print("Name: Abd Al-rahman Ahmed Mohammed Mahmoud\nID: 20211048")
    try:
        print("=" * 80)
        print("Welcome to the Modified Newton’s Method Solver")
        print("=" * 80)
        print("Choose an option:")
        print("1 - Solve a function using Newton's Method")
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
