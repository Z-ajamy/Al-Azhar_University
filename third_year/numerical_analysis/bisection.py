"""
Name: Abd Al-rahman Ahmed Mohammed Mahmoud
ID: 20211048
"""

import math
import sys

def compute_polynomial_value(polynomial_terms, x):
    """
    Evaluates the polynomial at a given value x.

    Parameters:
        polynomial_terms (list): List of tuples (coefficient, exponent).
        x (float): Point at which the function is evaluated.

    Returns:
        float: The result of f(x).
    """
    result = 0.0
    for coefficient, exponent in polynomial_terms:
        try:
            result += coefficient * math.pow(x, exponent)
        except ValueError as e:
            print(f"\n[Error] Failed to evaluate term ({coefficient}, {exponent}) at x = {x}: {e}")
            print("Ensure that x is suitable for the given exponents (e.g., x > 0 for fractional exponents).")
            sys.exit(1)
    return result

def find_root_bisection_method(polynomial_terms, interval_start, interval_end, precision_digits):
    """
    Uses the Bisection Method to approximate a root of the polynomial.

    Parameters:
        polynomial_terms (list): Polynomial terms as (coefficient, exponent).
        interval_start (float): Start of the interval.
        interval_end (float): End of the interval.
        precision_digits (int): Number of decimal places for accuracy.
    """
    tolerance = 10 ** -precision_digits

    if interval_end <= interval_start:
        print("[Error] Invalid interval: Start must be less than end.")
        return

    try:
        max_iterations = max(1, math.ceil(math.log((interval_end - interval_start) / tolerance) / math.log(2)))
    except ValueError as err:
        print(f"[Error] Failed to compute iteration count: {err}")
        sys.exit(1)

    print("\n" + "-" * 78)
    print(f"{'Iteration':<10} | {'Start (a)':<15} | {'End (b)':<15} | {'Midpoint (c)':<15} | {'f(c)':<15}")
    print("-" * 78)

    midpoint = interval_start
    for i in range(max_iterations):
        midpoint = (interval_start + interval_end) / 2.0
        f_mid = compute_polynomial_value(polynomial_terms, midpoint)

        print(f"{i + 1:<10} | {interval_start:<15.8f} | {interval_end:<15.8f} | {midpoint:<15.8f} | {f_mid:<15.8f}")

        if f_mid == 0.0:
            print("\n[Success] Exact root found: f(midpoint) = 0.")
            break

        f_start = compute_polynomial_value(polynomial_terms, interval_start)
        if f_start * f_mid < 0:
            interval_end = midpoint
        else:
            interval_start = midpoint
    else:
        print(f"\n[Info] Maximum number of iterations reached ({max_iterations}).")

    print("-" * 78)
    print(f"\n[Result] Approximated root: x = {midpoint:.{precision_digits + 4}f}")
    print(f"         f(x) ≈ {compute_polynomial_value(polynomial_terms, midpoint):.2e}")

if __name__ == "__main__":
    print("=== Polynomial Root Finder using Bisection Method ===\n")
    polynomial_terms = []

    try:
        num_terms = int(input("Enter the number of terms in the polynomial: "))
        if num_terms <= 0:
            print("[Error] The number of terms must be a positive integer.")
            sys.exit(1)

        print("\nProvide the terms as: coefficient and exponent (e.g., 2, 3 for 2x^3)")
        for i in range(num_terms):
            while True:
                try:
                    coefficient = float(input(f"  Coefficient for term {i + 1}: "))
                    exponent = int(input(f"  Exponent    for term {i + 1}: "))
                    polynomial_terms.append((coefficient, exponent))
                    break
                except ValueError:
                    print("  [Warning] Invalid input. Coefficient must be a number and exponent must be an integer.")

        print("\nSpecify the interval to search for a root:")
        while True:
            try:
                interval_start = float(input("  Start of interval (a): "))
                interval_end = float(input("  End of interval   (b): "))
                if interval_start >= interval_end:
                    print("  [Error] 'Start' must be less than 'End'.")
                else:
                    break
            except ValueError:
                print("  [Warning] Please enter valid numbers for the interval.")

        while True:
            try:
                precision_digits = int(input("\nEnter desired accuracy (e.g., enter 6 for 10^-6): "))
                if precision_digits <= 0:
                    print("  [Error] Precision must be a positive integer.")
                else:
                    break
            except ValueError:
                print("  [Warning] Please enter a valid integer.")

        f_start = compute_polynomial_value(polynomial_terms, interval_start)
        f_end = compute_polynomial_value(polynomial_terms, interval_end)

        print(f"\nInitial function evaluations:")
        print(f"  f({interval_start}) = {f_start:.6f}")
        print(f"  f({interval_end}) = {f_end:.6f}")

        if f_start == 0.0:
            print(f"\n[Result] Root found at start of interval: x = {interval_start}")
        elif f_end == 0.0:
            print(f"\n[Result] Root found at end of interval: x = {interval_end}")
        elif f_start * f_end > 0:
            print("\n[Error] f(a) and f(b) must have opposite signs.")
            print("        The function must cross the x-axis within the interval.")
        else:
            print("\n[Process] Initiating Bisection Method...\n")
            find_root_bisection_method(polynomial_terms, interval_start, interval_end, precision_digits)

    except ValueError:
        print("\n[Error] Invalid input. Please use numeric values where appropriate.")
    except KeyboardInterrupt:
        print("\n[Interrupted] Operation cancelled by user.")
    except Exception as err:
        print(f"\n[Unexpected Error] {err}")
